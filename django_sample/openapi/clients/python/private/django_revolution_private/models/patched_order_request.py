from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.patched_order_request_status import PatchedOrderRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOrderRequest")


@_attrs_define
class PatchedOrderRequest:
    """Serializer for Order model.

    Attributes:
        order_number (Union[Unset, str]):
        status (Union[Unset, PatchedOrderRequestStatus]): * `pending` - Pending
            * `processing` - Processing
            * `shipped` - Shipped
            * `delivered` - Delivered
            * `cancelled` - Cancelled
        total_amount (Union[Unset, str]):
    """

    order_number: Union[Unset, str] = UNSET
    status: Union[Unset, PatchedOrderRequestStatus] = UNSET
    total_amount: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_number = self.order_number

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_number is not UNSET:
            field_dict["order_number"] = order_number
        if status is not UNSET:
            field_dict["status"] = status
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.order_number, Unset):
            files.append(("order_number", (None, str(self.order_number).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.total_amount, Unset):
            files.append(("total_amount", (None, str(self.total_amount).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_number = d.pop("order_number", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedOrderRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedOrderRequestStatus(_status)

        total_amount = d.pop("total_amount", UNSET)

        patched_order_request = cls(
            order_number=order_number,
            status=status,
            total_amount=total_amount,
        )

        patched_order_request.additional_properties = d
        return patched_order_request

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
