"""
Django settings for Django Revolution tests.
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-test-key-for-testing-only-do-not-use-in-production"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "django_revolution",
    # Test apps
    "apps.users",
    "apps.public_api",
    "apps.private_api",
    "apps.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test_db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom User Model
AUTH_USER_MODEL = "users.User"

# Django Unfold Configuration
# ======================================
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Django Revolution Admin",
    "SITE_HEADER": "Django Revolution",
    "SITE_SUBHEADER": "Zone-based API Client Generator",
    "SITE_SYMBOL": "rocket_launch",
    "SITE_URL": "/",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": False,
    "THEME": "dark",  # Force dark theme
    "BORDER_RADIUS": "8px",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("API Management"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("Public API"),
                        "icon": "public",
                        "link": reverse_lazy("admin:public_api_post_changelist"),
                    },
                    {
                        "title": _("Private API"),
                        "icon": "business",
                        "link": reverse_lazy("admin:private_api_category_changelist"),
                    },
                ],
            },
            {
                "title": _("Documentation"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Swagger UI"),
                        "icon": "description",
                        "link": "/schema/public/schema/swagger/",
                    },
                    {
                        "title": _("OpenAPI Schema"),
                        "icon": "code",
                        "link": "/schema/public/schema/",
                    },
                ],
            },
        ],
    },
    "SITE_DROPDOWN": [
        {
            "icon": "home",
            "title": _("Home"),
            "link": "/",
        },
        {
            "icon": "api",
            "title": _("API Documentation"),
            "link": "/schema/public/schema/swagger/",
        },
        {
            "icon": "code",
            "title": _("Generated Clients"),
            "link": "/openapi/archive/",
        },
    ],
}

# Django Revolution Configuration
# ======================================

# 1. DRF + Spectacular Configuration (like in services.py)
from django_revolution.drf_config import create_drf_config
from django_revolution.config import MonorepoConfig, MonorepoSettings

drf_config = create_drf_config(
    title="Django Revolution Test API",
    description="Test API for Django Revolution with zone-based architecture",
    version="1.0.0",
    schema_path_prefix="/api/",
    enable_browsable_api=True,
    enable_throttling=True,
)

# Apply DRF and Spectacular settings
settings_dict = drf_config.get_django_settings()
REST_FRAMEWORK = settings_dict["REST_FRAMEWORK"]
# SPECTACULAR_SETTINGS = settings_dict['SPECTACULAR_SETTINGS']

# 2. Zone Configuration (like in revolution.py)
from django_revolution.app_config import ZoneConfig, get_revolution_config


def create_revolution_config() -> dict:
    """Get Django Revolution configuration as dictionary."""

    # Define zones with typed Pydantic models
    zones = {
        "accounts": ZoneConfig(
            apps=["apps.users"],
            title="Accounts API",
            description="User authentication and profile management",
            public=True,
            auth_required=False,
            version="v1",
        ),
        "public": ZoneConfig(
            apps=["apps.public_api"],
            title="Public API",
            description="Public API for testing - posts and content",
            public=True,
            auth_required=False,
            version="v1",
        ),
        "private": ZoneConfig(
            apps=["apps.private_api"],
            title="Private API",
            description="Private API for testing - categories, products, orders",
            public=False,
            auth_required=True,
            version="v1",
        ),
    }

    # Multi-monorepo configuration
    monorepo_settings = MonorepoSettings(
        enabled=True,
        configurations=[
            # Main frontend monorepo (only this one enabled)
            MonorepoConfig(
                name="frontend",
                enabled=True,
                path=str(BASE_DIR.parent / 'monorepo'),
                api_package_path='packages/api/src'
            ),
        ]
    )
    
    return get_revolution_config(project_root=BASE_DIR, zones=zones, debug=DEBUG, monorepo=monorepo_settings, api_prefix="api")


# Apply Django Revolution settings
DJANGO_REVOLUTION = create_revolution_config()

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    'https://revolution.unrealos.com',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),  # 24 hours
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),   # 7 days
}
