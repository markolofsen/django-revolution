from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Main router
router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]