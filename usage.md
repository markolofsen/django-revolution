---
layout: default
title: Usage
---

# Usage Guide

**How to use Django Revolution in your projects.**

## 🚀 Basic Usage

### Generate Clients

```bash
# Interactive generation (recommended)
python manage.py revolution

# Generate specific zones
python manage.py revolution --zones public admin

# TypeScript only
python manage.py revolution --typescript

# Python only
python manage.py revolution --python

# Skip archive creation
python manage.py revolution --no-archive
```

### Use TypeScript Clients

```typescript
import API from '@myorg/api-client';

const api = new API('https://api.example.com');

// Authentication
api.setToken('your-access-token', 'your-refresh-token');

// Call endpoints
const profile = await api.public.getCurrentUser();
const products = await api.public.listProducts();

// Check auth status
if (api.isAuthenticated()) {
  console.log('User is logged in');
}

// Automatic token refresh
api.onTokenRefresh((newToken) => {
  console.log('Token refreshed:', newToken);
});
```

### Use Python Clients

```python
from openapi.clients.python.public import PublicAPI

api = PublicAPI(base_url="https://api.example.com")
api.set_token("your-token-here")

# Call endpoints
profile = api.accounts.get_current_user()
products = api.products.list()

# Handle authentication
if api.is_authenticated():
    print("User is logged in")
```

## 🧩 Zone Configuration

### Define Zones with Pydantic Models

```python
# settings.py
from django_revolution.app_config import ZoneConfig, get_revolution_config

# Define zones with typed Pydantic models
zones = {
    'public': ZoneConfig(
        apps=['accounts', 'billing', 'payments'],
        title='Public API',
        description='API for public client applications',
        public=True,
        auth_required=False,
        version='v1',
        path_prefix='public'
    ),
    'admin': ZoneConfig(
        apps=['admin_panel', 'analytics'],
        title='Admin API',
        description='Administrative API endpoints',
        public=False,
        auth_required=True,
        version='v1',
        path_prefix='admin'
    ),
    'internal': ZoneConfig(
        apps=['system', 'mailer'],
        title='Internal API',
        description='Internal API for backend services',
        public=False,
        auth_required=True,
        version='v1',
        path_prefix='internal'
    )
}

# Configure Django Revolution
DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    debug=DEBUG
)
```

### Zone Properties

| Property        | Type | Required | Description                 |
| --------------- | ---- | -------- | --------------------------- |
| `apps`          | list | ✅       | Django apps to include      |
| `title`         | str  | ❌       | Human-readable title        |
| `description`   | str  | ❌       | Zone description            |
| `public`        | bool | ❌       | Is zone publicly accessible |
| `auth_required` | bool | ❌       | Requires authentication     |
| `version`       | str  | ❌       | API version (default: 'v1') |
| `path_prefix`   | str  | ❌       | URL path prefix             |

## 🔧 DRF + Spectacular Configuration

### Easy Configuration with Ready-to-Use Configs

Django Revolution provides **pre-built Pydantic configurations** that you can import and use directly:

#### **DRF + Spectacular Configuration** (services.py)

```python
# api/settings/config/services.py
from django_revolution.drf_config import create_drf_config

class SpectacularConfig(BaseModel):
    """API documentation configuration using django_revolution DRF config."""

    title: str = Field(default='API')
    description: str = Field(default='RESTful API')
    version: str = Field(default='1.0.0')
    schema_path_prefix: str = Field(default='/apix/')
    enable_browsable_api: bool = Field(default=False)
    enable_throttling: bool = Field(default=False)

    def get_django_settings(self) -> Dict[str, Any]:
        """Get drf-spectacular settings using django_revolution config."""
        # Use django_revolution DRF config - zero boilerplate!
        drf_config = create_drf_config(
            title=self.title,
            description=self.description,
            version=self.version,
            schema_path_prefix=self.schema_path_prefix,
            enable_browsable_api=self.enable_browsable_api,
            enable_throttling=self.enable_throttling,
        )

        return drf_config.get_django_settings()
```

## 🛠️ Development Workflow

### Interactive Development

```bash
# Start development CLI
python scripts/dev_cli.py

# Choose from:
# - 📦 Version Management
# - 🚀 Package Publishing
# - 🧪 Test Generation
# - 📋 Requirements Generation
# - 🔧 Package Building
```

### Version Management

```bash
# Get current version
python scripts/version_manager.py get

# Bump version
python scripts/version_manager.py bump --bump-type patch
python scripts/version_manager.py bump --bump-type minor
python scripts/version_manager.py bump --bump-type major

# Validate versions
python scripts/version_manager.py validate

# Regenerate requirements
python scripts/version_manager.py requirements
```

### Testing and Validation

```bash
# Validate zones
python manage.py revolution --validate-zones

# Show zone URLs
python manage.py revolution --show-urls

# Test schema generation
python manage.py revolution --test-schemas

# Check status
python manage.py revolution --status
```

### Publishing

```bash
# Interactive publishing
python scripts/publisher.py

# Choose repository (PyPI/TestPyPI)
# Automatic version bumping
# Build artifact cleanup
```

## 📦 Monorepo Integration (Optional)

### With Monorepo

```python
# settings.py - With monorepo integration
from django_revolution.app_config import MonorepoConfig

monorepo = MonorepoConfig(
    enabled=True,
    path=str(BASE_DIR.parent.parent / 'monorepo'),
    api_package_path='packages/api/src'
)

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    monorepo=monorepo
)
```

**Auto-generated monorepo structure:**

```yaml
monorepo/
├── packages/
│   └── api/
│       ├── src/
│       │   ├── index.ts          # Main client export
│       │   ├── public.ts         # Public zone client
│       │   ├── admin.ts          # Admin zone client
│       │   └── types.ts          # Shared types
│       ├── package.json          # NPM package
│       └── README.md             # Auto-generated docs
└── package.json                  # Workspace config
```

### Without Monorepo

```python
# settings.py - Simple setup
DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones
)
```

## 🎯 Advanced Usage

### Custom Output Configuration

```python
# settings.py
DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    output_config={
        'base_directory': 'custom_openapi',
        'typescript': {
            'enabled': True,
            'output_dir': 'custom_ts_clients',
            'package_name': '@myorg/custom-api'
        },
        'python': {
            'enabled': True,
            'output_dir': 'custom_py_clients',
            'package_name': 'myorg_custom_api'
        },
        'archive': {
            'enabled': True,
            'format': 'zip',
            'include_schemas': True
        }
    }
)
```

### Environment-Specific Configuration

```python
# settings.py
import os

# Different zones for different environments
if os.environ.get('DJANGO_ENV') == 'production':
    zones = {
        'public': ZoneConfig(
            apps=['accounts', 'billing'],
            title='Production Public API',
            public=True,
            auth_required=False
        )
    }
else:
    zones = {
        'public': ZoneConfig(
            apps=['accounts', 'billing', 'payments', 'support'],
            title='Development Public API',
            public=True,
            auth_required=False
        ),
        'dev': ZoneConfig(
            apps=['dev_tools', 'testing'],
            title='Development Tools API',
            public=False,
            auth_required=True
        )
    }
```

## 🔍 Troubleshooting

### Common Issues

```bash
# Check zone configuration
python manage.py revolution --validate-zones

# Test schema generation
python manage.py revolution --test-schemas

# Show detailed status
python manage.py revolution --status

# Clean and regenerate
python manage.py revolution --clean
python manage.py revolution
```

### Debug Mode

```bash
# Enable debug mode
export DJANGO_REVOLUTION_DEBUG=1

# Run with debug output
python manage.py revolution --debug
```

---

[← Back to Installation](installation.html) | [Next: CLI Reference →](cli.html)
