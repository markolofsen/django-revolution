from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product import Product


T = TypeVar("T", bound="OrderItem")


@_attrs_define
class OrderItem:
    """Serializer for OrderItem model.

    Attributes:
        id (int):
        product (Product): Serializer for Product model.
        quantity (int):
        price (str):
    """

    id: int
    product: "Product"
    quantity: int
    price: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        product = self.product.to_dict()

        quantity = self.quantity

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product": product,
                "quantity": quantity,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product import Product

        d = dict(src_dict)
        id = d.pop("id")

        product = Product.from_dict(d.pop("product"))

        quantity = d.pop("quantity")

        price = d.pop("price")

        order_item = cls(
            id=id,
            product=product,
            quantity=quantity,
            price=price,
        )

        order_item.additional_properties = d
        return order_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
