from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductRequest")


@_attrs_define
class ProductRequest:
    """Serializer for Product model.

    Attributes:
        name (str):
        description (str):
        price (str):
        stock (Union[Unset, int]):
    """

    name: str
    description: str
    price: str
    stock: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        price = self.price

        stock = self.stock

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "price": price,
            }
        )
        if stock is not UNSET:
            field_dict["stock"] = stock

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("description", (None, str(self.description).encode(), "text/plain")))

        files.append(("price", (None, str(self.price).encode(), "text/plain")))

        if not isinstance(self.stock, Unset):
            files.append(("stock", (None, str(self.stock).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        price = d.pop("price")

        stock = d.pop("stock", UNSET)

        product_request = cls(
            name=name,
            description=description,
            price=price,
            stock=stock,
        )

        product_request.additional_properties = d
        return product_request

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
