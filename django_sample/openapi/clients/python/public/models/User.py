from typing import *

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    None model
        Serializer for User model.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    username: str = Field(validation_alias="username")

    email: Optional[str] = Field(validation_alias="email", default=None)

    first_name: Optional[str] = Field(validation_alias="first_name", default=None)

    last_name: Optional[str] = Field(validation_alias="last_name", default=None)

    date_joined: str = Field(validation_alias="date_joined")
