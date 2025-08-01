from typing import *

from pydantic import BaseModel, Field

from .OrderItem import OrderItem
from .StatusEnum import StatusEnum


class PatchedOrder(BaseModel):
    """
    None model
        Serializer for Order model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[int] = Field(validation_alias="id", default=None)

    order_number: Optional[str] = Field(validation_alias="order_number", default=None)

    status: Optional[StatusEnum] = Field(validation_alias="status", default=None)

    total_amount: Optional[str] = Field(validation_alias="total_amount", default=None)

    created_at: Optional[str] = Field(validation_alias="created_at", default=None)

    items: Optional[List[Optional[OrderItem]]] = Field(validation_alias="items", default=None)
