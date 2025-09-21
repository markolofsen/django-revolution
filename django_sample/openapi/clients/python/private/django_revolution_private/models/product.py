import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """Serializer for Product model.

    Attributes:
        id (int):
        name (str):
        description (str):
        price (str):
        category (Category): Serializer for Category model.
        created_at (datetime.datetime):
        stock (Union[Unset, int]):
    """

    id: int
    name: str
    description: str
    price: str
    category: "Category"
    created_at: datetime.datetime
    stock: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        price = self.price

        category = self.category.to_dict()

        created_at = self.created_at.isoformat()

        stock = self.stock

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "price": price,
                "category": category,
                "created_at": created_at,
            }
        )
        if stock is not UNSET:
            field_dict["stock"] = stock

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        price = d.pop("price")

        category = Category.from_dict(d.pop("category"))

        created_at = isoparse(d.pop("created_at"))

        stock = d.pop("stock", UNSET)

        product = cls(
            id=id,
            name=name,
            description=description,
            price=price,
            category=category,
            created_at=created_at,
            stock=stock,
        )

        product.additional_properties = d
        return product

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
