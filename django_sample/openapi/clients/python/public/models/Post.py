from typing import *

from pydantic import BaseModel, Field

from .User import User


class Post(BaseModel):
    """
    None model
        Serializer for Post model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    title: str = Field(validation_alias="title")

    content: str = Field(validation_alias="content")

    author: User = Field(validation_alias="author")

    author_id: int = Field(validation_alias="author_id")

    published: Optional[bool] = Field(validation_alias="published", default=None)

    created_at: str = Field(validation_alias="created_at")
