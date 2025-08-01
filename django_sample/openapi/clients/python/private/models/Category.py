from typing import *

from pydantic import BaseModel, Field


class Category(BaseModel):
    """
    None model
        Serializer for Category model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    name: str = Field(validation_alias="name")

    description: Optional[str] = Field(validation_alias="description", default=None)

    is_active: Optional[bool] = Field(validation_alias="is_active", default=None)
