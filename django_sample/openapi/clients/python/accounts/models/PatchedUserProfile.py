from typing import *

from pydantic import BaseModel, Field


class PatchedUserProfile(BaseModel):
    """
    None model
        Serializer for user profile with minimal fields.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[int] = Field(validation_alias="id", default=None)

    username: Optional[str] = Field(validation_alias="username", default=None)

    email: Optional[str] = Field(validation_alias="email", default=None)

    first_name: Optional[str] = Field(validation_alias="first_name", default=None)

    last_name: Optional[str] = Field(validation_alias="last_name", default=None)

    full_name: Optional[str] = Field(validation_alias="full_name", default=None)

    display_name: Optional[str] = Field(validation_alias="display_name", default=None)

    bio: Optional[str] = Field(validation_alias="bio", default=None)

    avatar: Optional[str] = Field(validation_alias="avatar", default=None)

    phone: Optional[str] = Field(validation_alias="phone", default=None)

    website: Optional[str] = Field(validation_alias="website", default=None)

    location: Optional[str] = Field(validation_alias="location", default=None)

    is_verified: Optional[bool] = Field(validation_alias="is_verified", default=None)

    date_joined: Optional[str] = Field(validation_alias="date_joined", default=None)
