from typing import *

from pydantic import BaseModel, Field

from .Product import Product


class PatchedOrderItem(BaseModel):
    """
    None model
        Serializer for OrderItem model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[int] = Field(validation_alias="id", default=None)

    product: Optional[Product] = Field(validation_alias="product", default=None)

    quantity: Optional[int] = Field(validation_alias="quantity", default=None)

    price: Optional[str] = Field(validation_alias="price", default=None)
