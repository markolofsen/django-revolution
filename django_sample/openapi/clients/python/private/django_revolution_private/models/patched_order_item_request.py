from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOrderItemRequest")


@_attrs_define
class PatchedOrderItemRequest:
    """Serializer for OrderItem model.

    Attributes:
        quantity (Union[Unset, int]):
        price (Union[Unset, str]):
    """

    quantity: Union[Unset, int] = UNSET
    price: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.quantity, Unset):
            files.append(("quantity", (None, str(self.quantity).encode(), "text/plain")))

        if not isinstance(self.price, Unset):
            files.append(("price", (None, str(self.price).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity", UNSET)

        price = d.pop("price", UNSET)

        patched_order_item_request = cls(
            quantity=quantity,
            price=price,
        )

        patched_order_item_request.additional_properties = d
        return patched_order_item_request

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
