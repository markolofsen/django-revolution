from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProductRequest")


@_attrs_define
class PatchedProductRequest:
    """Serializer for Product model.

    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        price (Union[Unset, str]):
        stock (Union[Unset, int]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    stock: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        price = self.price

        stock = self.stock

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if price is not UNSET:
            field_dict["price"] = price
        if stock is not UNSET:
            field_dict["stock"] = stock

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.price, Unset):
            files.append(("price", (None, str(self.price).encode(), "text/plain")))

        if not isinstance(self.stock, Unset):
            files.append(("stock", (None, str(self.stock).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        price = d.pop("price", UNSET)

        stock = d.pop("stock", UNSET)

        patched_product_request = cls(
            name=name,
            description=description,
            price=price,
            stock=stock,
        )

        patched_product_request.additional_properties = d
        return patched_product_request

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
