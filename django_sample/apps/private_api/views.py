from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import Category, Product, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for Category model with nested routing and drf-spectacular documentation."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        """Filter categories if needed."""
        queryset = super().get_queryset()
        # Add any filtering logic here if needed
        return queryset
    
    @extend_schema(
        summary="Get active categories",
        description="Returns only active categories",
        responses={200: CategorySerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active categories."""
        categories = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Get category products",
        description="Returns all products in specific category",
        responses={200: ProductSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """Get all products in category."""
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for Product model with nested routing."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        """Filter products by category if category_id is provided."""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_pk')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset.select_related('category')
    
    @extend_schema(
        summary="Get products by category",
        responses={200: ProductSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get products filtered by category."""
        category_id = request.query_params.get('category_id')
        if category_id:
            products = self.get_queryset().filter(category_id=category_id)
        else:
            products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Get low stock products",
        description="Returns products with stock less than 10",
        responses={200: ProductSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Get products with low stock."""
        products = self.get_queryset().filter(stock__lt=10)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Get product order items",
        description="Returns all order items for specific product",
        responses={200: OrderItemSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def order_items(self, request, pk=None):
        """Get all order items for product."""
        product = self.get_object()
        order_items = OrderItem.objects.filter(product=product)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)


class OrderItemViewSet(viewsets.ModelViewSet):
    """ViewSet for OrderItem model with nested routing."""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        """Filter order items by order or product if provided."""
        queryset = super().get_queryset()
        order_id = self.kwargs.get('order_pk')
        product_id = self.kwargs.get('product_pk')
        
        if order_id:
            queryset = queryset.filter(order_id=order_id)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
            
        return queryset.select_related('order', 'product')


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for Order model with nested routing."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        """Get orders with prefetched items."""
        return super().get_queryset().prefetch_related('items')
    
    @extend_schema(
        summary="Get orders by status",
        parameters=[
            OpenApiParameter(name='status', type=str, location=OpenApiParameter.QUERY)
        ],
        responses={200: OrderSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def by_status(self, request):
        """Get orders filtered by status."""
        status_param = request.query_params.get('status')
        if status_param:
            orders = self.get_queryset().filter(status=status_param)
        else:
            orders = self.get_queryset()
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Cancel order",
        responses={200: OrderSerializer}
    )
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Cancel an order."""
        order = self.get_object()
        order.status = 'cancelled'
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Get order items",
        description="Returns all items in specific order",
        responses={200: OrderItemSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        """Get all items in order."""
        order = self.get_object()
        order_items = order.items.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data) 