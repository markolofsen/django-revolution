import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.order_status import OrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_item import OrderItem


T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """Serializer for Order model.

    Attributes:
        id (int):
        order_number (str):
        total_amount (str):
        created_at (datetime.datetime):
        items (list['OrderItem']):
        status (Union[Unset, OrderStatus]): * `pending` - Pending
            * `processing` - Processing
            * `shipped` - Shipped
            * `delivered` - Delivered
            * `cancelled` - Cancelled
    """

    id: int
    order_number: str
    total_amount: str
    created_at: datetime.datetime
    items: list["OrderItem"]
    status: Union[Unset, OrderStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order_number = self.order_number

        total_amount = self.total_amount

        created_at = self.created_at.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order_number": order_number,
                "total_amount": total_amount,
                "created_at": created_at,
                "items": items,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_item import OrderItem

        d = dict(src_dict)
        id = d.pop("id")

        order_number = d.pop("order_number")

        total_amount = d.pop("total_amount")

        created_at = isoparse(d.pop("created_at"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderStatus(_status)

        order = cls(
            id=id,
            order_number=order_number,
            total_amount=total_amount,
            created_at=created_at,
            items=items,
            status=status,
        )

        order.additional_properties = d
        return order

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
