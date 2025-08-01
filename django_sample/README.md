# Django Revolution - Sample Project

This is a test Django project for Django Revolution, demonstrating zone-based API client generation with automatic configuration.

## Quick Start

### Prerequisites

- Python 3.10+
- Poetry (for dependency management)
- Django 5.2+
- Django REST Framework
- drf-spectacular

### Installation & Setup

1. **Install dependencies:**

   ```bash
   poetry install
   ```

2. **Run migrations:**

   ```bash
   poetry run python manage.py migrate
   ```

3. **Start the development server:**

   ```bash
   poetry run python manage.py runserver
   ```

4. **Access the API:**

   - **Swagger UI (Public API):** http://localhost:8000/schema/public/schema/swagger/
   - **Swagger UI (Private API):** http://localhost:8000/schema/private/schema/swagger/
   - **Redoc UI (Public API):** http://localhost:8000/schema/public/redoc/
   - **Redoc UI (Private API):** http://localhost:8000/schema/private/redoc/
   - **Public API endpoints:** http://localhost:8000/api/public/
   - **Private API endpoints:** http://localhost:8000/api/private/

5. **CORS Configuration:**

   The project includes CORS configuration for frontend development:
   - Allowed origins: `http://localhost:3000`, `http://localhost:3001`
   - Credentials allowed
   - All common HTTP methods and headers supported

## Client Generation

### Generate All Clients

```bash
poetry run python manage.py auto_generate
```

### Generate Specific Zones

```bash
# Generate only public zone
poetry run python manage.py auto_generate --zones public

# Generate only private zone  
poetry run python manage.py auto_generate --zones private

# Generate both zones
poetry run python manage.py auto_generate --zones public private
```

### Generate Specific Client Types

```bash
# TypeScript only
poetry run python manage.py auto_generate --typescript-only

# Python only
poetry run python manage.py auto_generate --python-only
```

### Clean Generation

```bash
# Clean output directories before generation
poetry run python manage.py auto_generate --clean
```

### Skip Archiving

```bash
# Generate without creating archives
poetry run python manage.py auto_generate --no-archive
```

## Project Structure

```
django_sample/
├── apps/
│   ├── public_api/          # Public API zone
│   │   ├── models.py        # User, Post models
│   │   ├── views.py         # ViewSets
│   │   ├── urls.py          # URL patterns
│   │   └── serializers.py   # DRF serializers
│   ├── private_api/         # Private API zone
│   │   ├── models.py        # Category, Product, Order models
│   │   ├── views.py         # ViewSets
│   │   ├── urls.py          # URL patterns
│   │   └── serializers.py   # DRF serializers
│   └── core/                # Core app with management commands
│       └── management/
│           └── commands/
│               └── auto_generate.py  # Client generation command
├── settings.py              # Django settings with automatic config
├── urls.py                  # Main URL configuration
├── pyproject.toml           # Poetry dependencies
└── openapi/                 # Generated clients and schemas
    ├── schemas/             # OpenAPI schemas
    ├── clients/             # Generated clients
    └── archive/             # Archived clients
```

## Configuration

### 1. DRF + Spectacular Configuration

```python
# settings.py - Automatic DRF configuration
from django_revolution.drf_config import create_drf_config

drf_config = create_drf_config(
    title="Django Revolution Test API",
    description="Test API for Django Revolution with zone-based architecture",
    version="1.0.0",
    schema_path_prefix="/api/",
    enable_browsable_api=True,
    enable_throttling=True,
)

# Apply settings automatically
settings_dict = drf_config.get_django_settings()
REST_FRAMEWORK = settings_dict["REST_FRAMEWORK"]
SPECTACULAR_SETTINGS = settings_dict["SPECTACULAR_SETTINGS"]
```

### 2. Zone Configuration

```python
# settings.py - Zone configuration with Pydantic models
from django_revolution.app_config import ZoneConfig, get_revolution_config
from django_revolution.app_config import MonorepoConfig

def create_revolution_config() -> dict:
    """Get Django Revolution configuration as dictionary."""

    zones = {
        'public': ZoneConfig(
            apps=['apps.public_api'],
            title='Public API',
            description='Public API for testing - users and posts',
            public=True,
            auth_required=False,
            version='v1'
        ),
        'private': ZoneConfig(
            apps=['apps.private_api'],
            title='Private API',
            description='Private API for testing - categories, products, orders',
            public=False,
            auth_required=True,
            version='v1'
        )
    }

    # With monorepo sync enabled
    monorepo = MonorepoConfig(
        enabled=True,
        path=str(BASE_DIR.parent / 'monorepo'),
        api_package_path='packages/api/src'
    )
    return get_revolution_config(
        project_root=BASE_DIR, 
        zones=zones, 
        debug=DEBUG,
        monorepo=monorepo,
        api_prefix="api"
    )

# Apply Django Revolution settings
DJANGO_REVOLUTION = create_revolution_config()
```

### 3. URL Integration

```python
# urls.py - Automatic URL generation
from django_revolution import add_revolution_urls

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Root redirect to Swagger UI
    path("", RedirectView.as_view(url="/schema/public/schema/swagger/", permanent=False)),
]

# Django Revolution automatically adds:
# - /schema/public/schema/ (OpenAPI spec)
# - /schema/public/schema/swagger/ (Swagger UI)
# - /schema/private/schema/ (OpenAPI spec)
# - /schema/private/schema/swagger/ (Swagger UI)
# - /api/public/ (Public API endpoints)
# - /api/private/ (Private API endpoints)
# - /openapi/archive/ (Generated clients)
urlpatterns = add_revolution_urls(urlpatterns)
```

## API Zones

The project demonstrates two API zones:

### Public Zone

- **Apps:** `apps.public_api`
- **Models:** User, Post
- **Endpoints:** `/api/public/users/`, `/api/public/posts/`
- **Access:** Public, no auth required
- **Schema:** `/schema/public/schema/swagger/`

### Private Zone

- **Apps:** `apps.private_api`
- **Models:** Category, Product, Order, OrderItem
- **Endpoints:** `/api/private/categories/`, `/api/private/products/`, etc.
- **Access:** Private, auth required
- **Schema:** `/schema/private/schema/swagger/`

## Generated Clients

After running `poetry run python manage.py auto_generate`, you'll find:

### TypeScript Clients

- **Location:** `openapi/clients/typescript/`
- **Files:** API client, types, utilities
- **Usage:** Import and use in TypeScript/JavaScript projects

### Python Clients

- **Location:** `openapi/clients/python/`
- **Files:** Pydantic models, API client
- **Usage:** Import and use in Python projects

### Archives

- **Location:** `openapi/archive/`
- **Format:** ZIP files with versioned clients
- **Usage:** Distribution and deployment

### Monorepo Sync

- **Location:** `../monorepo/packages/api/src/typescript/`
- **Files:** TypeScript clients automatically synced to monorepo
- **Usage:** Import from `@unrealos/api` package in monorepo projects

## Development Workflow

1. **Make changes** to your Django models, views, or serializers
2. **Generate clients** with `poetry run python manage.py auto_generate`
3. **Test the API** using Swagger UI
4. **Use generated clients** in your frontend or other services

## Troubleshooting

### Static Files Not Loading

If Swagger UI static files don't load:

```bash
poetry run python manage.py collectstatic
```

### Generation Errors

Check that all required dependencies are installed:

```bash
poetry install
```

### Zone Configuration Issues

Verify your zone configuration in `settings.py` and ensure all apps are in `INSTALLED_APPS`.
