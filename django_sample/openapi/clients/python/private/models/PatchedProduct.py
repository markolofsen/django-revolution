from typing import *

from pydantic import BaseModel, Field

from .Category import Category


class PatchedProduct(BaseModel):
    """
    None model
        Serializer for Product model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[int] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    price: Optional[str] = Field(validation_alias="price", default=None)

    category: Optional[Category] = Field(validation_alias="category", default=None)

    stock: Optional[int] = Field(validation_alias="stock", default=None)

    created_at: Optional[str] = Field(validation_alias="created_at", default=None)
