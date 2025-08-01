from typing import *

from pydantic import BaseModel, Field

from .OrderItem import OrderItem
from .StatusEnum import StatusEnum


class Order(BaseModel):
    """
    None model
        Serializer for Order model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    order_number: str = Field(validation_alias="order_number")

    status: Optional[StatusEnum] = Field(validation_alias="status", default=None)

    total_amount: str = Field(validation_alias="total_amount")

    created_at: str = Field(validation_alias="created_at")

    items: List[OrderItem] = Field(validation_alias="items")
