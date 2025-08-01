from typing import *

from pydantic import BaseModel, Field

from .Product import Product


class OrderItem(BaseModel):
    """
    None model
        Serializer for OrderItem model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    product: Product = Field(validation_alias="product")

    quantity: int = Field(validation_alias="quantity")

    price: str = Field(validation_alias="price")
