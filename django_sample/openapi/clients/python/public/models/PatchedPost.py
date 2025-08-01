from typing import *

from pydantic import BaseModel, Field

from .User import User


class PatchedPost(BaseModel):
    """
    None model
        Serializer for Post model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[int] = Field(validation_alias="id", default=None)

    title: Optional[str] = Field(validation_alias="title", default=None)

    content: Optional[str] = Field(validation_alias="content", default=None)

    author: Optional[User] = Field(validation_alias="author", default=None)

    author_id: Optional[int] = Field(validation_alias="author_id", default=None)

    published: Optional[bool] = Field(validation_alias="published", default=None)

    created_at: Optional[str] = Field(validation_alias="created_at", default=None)
