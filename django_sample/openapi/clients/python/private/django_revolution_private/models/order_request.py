from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.order_request_status import OrderRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderRequest")


@_attrs_define
class OrderRequest:
    """Serializer for Order model.

    Attributes:
        order_number (str):
        total_amount (str):
        status (Union[Unset, OrderRequestStatus]): * `pending` - Pending
            * `processing` - Processing
            * `shipped` - Shipped
            * `delivered` - Delivered
            * `cancelled` - Cancelled
    """

    order_number: str
    total_amount: str
    status: Union[Unset, OrderRequestStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_number = self.order_number

        total_amount = self.total_amount

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_number": order_number,
                "total_amount": total_amount,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("order_number", (None, str(self.order_number).encode(), "text/plain")))

        files.append(("total_amount", (None, str(self.total_amount).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_number = d.pop("order_number")

        total_amount = d.pop("total_amount")

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderRequestStatus(_status)

        order_request = cls(
            order_number=order_number,
            total_amount=total_amount,
            status=status,
        )

        order_request.additional_properties = d
        return order_request

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
