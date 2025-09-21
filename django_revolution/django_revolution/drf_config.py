"""
Universal DRF Spectacular Configuration for Django Revolution

This module provides a Pydantic-based configuration for DRF Spectacular
that can be easily imported and used in Django projects.
"""

from typing import Dict, Any, Optional, List, Union
from pydantic import BaseModel, Field, ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict


class SwaggerUISettings(BaseModel):
    """Swagger UI settings configuration."""

    deepLinking: bool = Field(default=True, description="Enable deep linking")
    persistAuthorization: bool = Field(
        default=True, description="Persist authorization"
    )
    displayOperationId: bool = Field(default=False, description="Display operation ID")
    defaultModelsExpandDepth: int = Field(
        default=3, description="Default models expand depth"
    )
    defaultModelExpandDepth: int = Field(
        default=3, description="Default model expand depth"
    )
    defaultModelRendering: str = Field(
        default="model", description="Default model rendering"
    )
    displayRequestDuration: bool = Field(
        default=True, description="Display request duration"
    )
    docExpansion: str = Field(default="list", description="Documentation expansion")
    filter: bool = Field(default=True, description="Enable filtering")
    showExtensions: bool = Field(default=True, description="Show extensions")
    showCommonExtensions: bool = Field(
        default=True, description="Show common extensions"
    )
    tryItOutEnabled: bool = Field(default=True, description="Enable try it out")


class SpectacularSettings(BaseModel):
    """DRF Spectacular settings configuration."""

    title: str = Field(default="API", description="API title")
    description: str = Field(default="RESTful API", description="API description")
    version: str = Field(default="1.0.0", description="API version")
    terms_of_service: Optional[str] = Field(
        default=None, description="Terms of service URL"
    )
    contact: Optional[Dict[str, str]] = Field(
        default=None, description="Contact information"
    )
    license_info: Optional[Dict[str, str]] = Field(
        default=None, description="License information"
    )

    # Schema generation settings
    serve_include_schema: bool = Field(
        default=True, description="Include schema in serve"
    )
    schema_path_prefix: str = Field(default="/api/", description="Schema path prefix")
    component_split_request: bool = Field(
        default=True, description="Split request components"
    )
    component_split_response: bool = Field(
        default=True, description="Split response components"
    )
    component_no_read_only_required: bool = Field(
        default=False, description="No read-only required"
    )
    enum_add_explicit_blank_null_choice: bool = Field(
        default=False, description="Add explicit blank/null choice"
    )
    
    # Enum generation settings - CRITICAL for proper client generation
    generate_enum_from_choices: bool = Field(
        default=True, description="Generate enum components from Django choices"
    )
    enum_generate_choice_from_path: bool = Field(
        default=True, description="Generate enum components from path parameters"
    )
    enum_name_suffix: str = Field(
        default="Enum", description="Suffix for generated enum names"
    )
    camelize_names: bool = Field(
        default=False, description="Camelize enum and field names"
    )

    # Advanced settings
    enum_name_overrides: Dict[str, str] = Field(
        default_factory=dict, description="Enum name overrides"
    )
    schema_coerce_path_pk_suffix: bool = Field(
        default=True, description="Coerce path PK suffix"
    )
    schema_coerce_method_names: Dict[str, str] = Field(
        default_factory=lambda: {
            "retrieve": "get",
            "destroy": "delete",
            "partial_update": "patch",
            "update": "put",
        },
        description="Coerce method names for stable operation IDs"
    )
    schema_path_prefix_trim: bool = Field(
        default=False, description="Trim schema path prefix"
    )
    generator_class: str = Field(
        default="drf_spectacular.generators.SchemaGenerator",
        description="Generator class",
    )
    schema_generator_class: str = Field(
        default="drf_spectacular.generators.SchemaGenerator",
        description="Schema generator class",
    )

    # UI settings
    swagger_ui_settings: SwaggerUISettings = Field(
        default_factory=SwaggerUISettings, description="Swagger UI settings"
    )
    swagger_ui_dist: str = Field(
        default="SIDECAR", description="Swagger UI distribution"
    )
    swagger_ui_favicon_href: str = Field(
        default="SIDECAR", description="Swagger UI favicon"
    )
    redoc_dist: str = Field(default="SIDECAR", description="ReDoc distribution")

    # Processing hooks
    postprocessing_hooks: List[str] = Field(
        default_factory=list,
        description="Post-processing hooks"
    )
    preprocessing_hooks: List[str] = Field(
        default_factory=list,
        description="Pre-processing hooks"
    )
    
    # Additional stability settings
    disable_errors_and_warnings: bool = Field(default=False, description="Disable errors and warnings")
    operation_id_generator_class: Optional[str] = Field(
        default=None, 
        description="Custom operation ID generator class"
    )

    # Custom settings
    custom_settings: Dict[str, Any] = Field(
        default_factory=dict, description="Custom settings"
    )

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    def get_django_settings(self) -> Dict[str, Any]:
        """Convert to Django settings format."""
        settings = {
            "TITLE": self.title,
            "DESCRIPTION": self.description,
            "VERSION": self.version,
            "SERVE_INCLUDE_SCHEMA": self.serve_include_schema,
            "SCHEMA_PATH_PREFIX": self.schema_path_prefix,
            "COMPONENT_SPLIT_REQUEST": self.component_split_request,
            "COMPONENT_SPLIT_RESPONSE": self.component_split_response,
            "COMPONENT_NO_READ_ONLY_REQUIRED": self.component_no_read_only_required,
            "ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE": self.enum_add_explicit_blank_null_choice,
            
            # Enum generation settings - CRITICAL for proper client generation
            "GENERATE_ENUM_FROM_CHOICES": self.generate_enum_from_choices,
            "ENUM_GENERATE_CHOICE_FROM_PATH": self.enum_generate_choice_from_path,
            "ENUM_NAME_SUFFIX": self.enum_name_suffix,
            "CAMELIZE_NAMES": self.camelize_names,
            
            "ENUM_NAME_OVERRIDES": self.enum_name_overrides,
            "SCHEMA_COERCE_PATH_PK_SUFFIX": self.schema_coerce_path_pk_suffix,
            "SCHEMA_COERCE_METHOD_NAMES": self.schema_coerce_method_names,
            "SCHEMA_PATH_PREFIX_TRIM": self.schema_path_prefix_trim,
            "GENERATOR_CLASS": self.generator_class,
            "SCHEMA_GENERATOR_CLASS": self.schema_generator_class,
            "SWAGGER_UI_SETTINGS": self.swagger_ui_settings.model_dump(),
            "SWAGGER_UI_DIST": self.swagger_ui_dist,
            "SWAGGER_UI_FAVICON_HREF": self.swagger_ui_favicon_href,
            "REDOC_DIST": self.redoc_dist,
            # Processing hooks
            "POSTPROCESSING_HOOKS": self.postprocessing_hooks,
            "PREPROCESSING_HOOKS": self.preprocessing_hooks,
            # Stability settings
            "DISABLE_ERRORS_AND_WARNINGS": self.disable_errors_and_warnings,
        }

        # Add optional fields if provided
        if self.terms_of_service:
            settings["TERMS_OF_SERVICE"] = self.terms_of_service
        if self.contact:
            settings["CONTACT"] = self.contact
        if self.license_info:
            settings["LICENSE_INFO"] = self.license_info
        
        # Add optional operation ID generator
        if self.operation_id_generator_class:
            settings["OPERATION_ID_GENERATOR_CLASS"] = self.operation_id_generator_class

        # Add custom settings
        settings.update(self.custom_settings)

        return {"SPECTACULAR_SETTINGS": settings}


class DRFConfig(BaseModel):
    """Complete DRF configuration including Spectacular settings."""

    # REST Framework settings
    default_renderer_classes: List[str] = Field(
        default_factory=lambda: ["rest_framework.renderers.JSONRenderer"],
        description="Default renderer classes",
    )
    default_permission_classes: List[str] = Field(
        default_factory=lambda: [
            "rest_framework.permissions.AllowAny",
            "rest_framework.permissions.IsAuthenticated",
        ],
        description="Default permission classes",
    )
    default_authentication_classes: List[str] = Field(
        default_factory=lambda: [
            "rest_framework_simplejwt.authentication.JWTAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ],
        description="Default authentication classes",
    )
    default_filter_backends: List[str] = Field(
        default_factory=lambda: [
            "django_filters.rest_framework.DjangoFilterBackend",
            "rest_framework.filters.SearchFilter",
            "rest_framework.filters.OrderingFilter",
        ],
        description="Default filter backends",
    )
    page_size: int = Field(default=10, description="Default page size")
    enable_browsable_api: bool = Field(
        default=False, description="Enable browsable API"
    )
    enable_throttling: bool = Field(default=False, description="Enable throttling")
    anon_throttle_rate: str = Field(
        default="100/hour", description="Anonymous throttle rate"
    )
    user_throttle_rate: str = Field(
        default="1000/hour", description="User throttle rate"
    )

    # Spectacular settings
    spectacular: SpectacularSettings = Field(
        default_factory=SpectacularSettings, description="Spectacular settings"
    )

    # Custom settings
    custom_rest_framework_settings: Dict[str, Any] = Field(
        default_factory=dict, description="Custom REST framework settings"
    )

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    def get_django_settings(self) -> Dict[str, Any]:
        """Convert to Django settings format."""
        # REST Framework settings
        rest_framework = {
            "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
            "DEFAULT_RENDERER_CLASSES": self.default_renderer_classes.copy(),
            "DEFAULT_JSON_INDENT": 4,
            "DEFAULT_PERMISSION_CLASSES": self.default_permission_classes,
            "DEFAULT_AUTHENTICATION_CLASSES": self.default_authentication_classes,
            "DEFAULT_FILTER_BACKENDS": self.default_filter_backends,
            "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
            "PAGE_SIZE": self.page_size,
            "DEFAULT_PARSER_CLASSES": [
                "rest_framework.parsers.FormParser",
                "rest_framework.parsers.MultiPartParser",
                "rest_framework.parsers.JSONParser",
            ],
        }

        if self.enable_browsable_api:
            rest_framework["DEFAULT_RENDERER_CLASSES"].append(
                "rest_framework.renderers.BrowsableAPIRenderer"
            )

        if self.enable_throttling:
            rest_framework.update(
                {
                    "DEFAULT_THROTTLE_CLASSES": [
                        "rest_framework.throttling.AnonRateThrottle",
                        "rest_framework.throttling.UserRateThrottle",
                    ],
                    "DEFAULT_THROTTLE_RATES": {
                        "anon": self.anon_throttle_rate,
                        "user": self.user_throttle_rate,
                    },
                }
            )

        # Add custom REST framework settings
        rest_framework.update(self.custom_rest_framework_settings)

        # Combine all settings
        settings = {
            "REST_FRAMEWORK": rest_framework,
        }

        # Add Spectacular settings
        settings.update(self.spectacular.get_django_settings())

        return settings


# Convenience functions for easy usage
def create_spectacular_config(
    title: str = "API",
    description: str = "RESTful API",
    version: str = "1.0.0",
    schema_path_prefix: str = "/api/",
    **kwargs,
) -> SpectacularSettings:
    """
    Create a SpectacularSettings instance with common defaults.

    Args:
        title: API title
        description: API description
        version: API version
        schema_path_prefix: Schema path prefix
        **kwargs: Additional settings to override

    Returns:
        SpectacularSettings instance
    """
    return SpectacularSettings(
        title=title,
        description=description,
        version=version,
        schema_path_prefix=schema_path_prefix,
        **kwargs,
    )


def create_drf_config(
    title: str = "API",
    description: str = "RESTful API",
    version: str = "1.0.0",
    schema_path_prefix: str = "/api/",
    enable_browsable_api: bool = False,
    enable_throttling: bool = False,
    **kwargs,
) -> DRFConfig:
    """
    Create a DRFConfig instance with common defaults.

    Args:
        title: API title
        description: API description
        version: API version
        schema_path_prefix: Schema path prefix
        enable_browsable_api: Enable browsable API
        enable_throttling: Enable throttling
        **kwargs: Additional settings to override

    Returns:
        DRFConfig instance
    """
    spectacular = create_spectacular_config(
        title=title,
        description=description,
        version=version,
        schema_path_prefix=schema_path_prefix,
    )

    return DRFConfig(
        spectacular=spectacular,
        enable_browsable_api=enable_browsable_api,
        enable_throttling=enable_throttling,
        **kwargs,
    )


# Default configurations for common use cases
def get_default_spectacular_config() -> SpectacularSettings:
    """Get default Spectacular configuration optimized for client generation."""
    return SpectacularSettings(
        title="API",
        description="RESTful API",
        version="1.0.0",
        schema_path_prefix="/api/",
        component_split_request=True,
        component_split_response=True,
        enum_add_explicit_blank_null_choice=False,
        
        # Enum generation settings - CRITICAL for proper client generation
        generate_enum_from_choices=True,
        enum_generate_choice_from_path=True,
        enum_name_suffix="Enum",
        camelize_names=False,
        
        schema_coerce_path_pk_suffix=True,
        schema_coerce_method_names={
            "retrieve": "get",
            "destroy": "delete",
            "partial_update": "patch",
            "update": "put",
        },
        disable_errors_and_warnings=False,
    )


def get_default_drf_config() -> DRFConfig:
    """Get default DRF configuration optimized for client generation."""
    return DRFConfig(
        spectacular=get_default_spectacular_config(),
        enable_browsable_api=False,
        enable_throttling=False,
    )


# Export main classes and functions
__all__ = [
    "SpectacularSettings",
    "DRFConfig",
    "SwaggerUISettings",
    "create_spectacular_config",
    "create_drf_config",
    "get_default_spectacular_config",
    "get_default_drf_config",
]
