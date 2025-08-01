from typing import *

from pydantic import BaseModel, Field

from .Category import Category


class Product(BaseModel):
    """
    None model
        Serializer for Product model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    name: str = Field(validation_alias="name")

    description: str = Field(validation_alias="description")

    price: str = Field(validation_alias="price")

    category: Category = Field(validation_alias="category")

    stock: Optional[int] = Field(validation_alias="stock", default=None)

    created_at: str = Field(validation_alias="created_at")
