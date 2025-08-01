from typing import *

from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    """
    None model
        Serializer for user profile with minimal fields.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: int = Field(validation_alias="id")

    username: str = Field(validation_alias="username")

    email: str = Field(validation_alias="email")

    first_name: Optional[str] = Field(validation_alias="first_name", default=None)

    last_name: Optional[str] = Field(validation_alias="last_name", default=None)

    full_name: str = Field(validation_alias="full_name")

    display_name: str = Field(validation_alias="display_name")

    bio: Optional[str] = Field(validation_alias="bio", default=None)

    avatar: Optional[str] = Field(validation_alias="avatar", default=None)

    phone: Optional[str] = Field(validation_alias="phone", default=None)

    website: Optional[str] = Field(validation_alias="website", default=None)

    location: Optional[str] = Field(validation_alias="location", default=None)

    is_verified: bool = Field(validation_alias="is_verified")

    date_joined: str = Field(validation_alias="date_joined")
