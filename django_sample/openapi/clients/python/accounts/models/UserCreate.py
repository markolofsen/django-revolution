from typing import *

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """
    None model
        Serializer for user registration.

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    username: str = Field(validation_alias="username")

    email: Optional[str] = Field(validation_alias="email", default=None)

    password: str = Field(validation_alias="password")

    password_confirm: str = Field(validation_alias="password_confirm")

    first_name: Optional[str] = Field(validation_alias="first_name", default=None)

    last_name: Optional[str] = Field(validation_alias="last_name", default=None)

    bio: Optional[str] = Field(validation_alias="bio", default=None)

    avatar: Optional[str] = Field(validation_alias="avatar", default=None)

    phone: Optional[str] = Field(validation_alias="phone", default=None)

    date_of_birth: Optional[str] = Field(validation_alias="date_of_birth", default=None)

    website: Optional[str] = Field(validation_alias="website", default=None)

    location: Optional[str] = Field(validation_alias="location", default=None)

    email_notifications: Optional[bool] = Field(
        validation_alias="email_notifications", default=None
    )

    newsletter_subscription: Optional[bool] = Field(
        validation_alias="newsletter_subscription", default=None
    )
