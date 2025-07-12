---
layout: default
title: Usage
---

# Usage Guide

**How to use Django Revolution in your projects.**

## Basic Usage

### Generate Clients

```bash
# Generate all clients
python manage.py revolution

# Generate specific zones
python manage.py revolution --zones public admin

# TypeScript only
python manage.py revolution --typescript
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
```

### Use Python Clients

```python
from openapi.clients.python.public import PublicAPI

api = PublicAPI(base_url="https://api.example.com")
api.set_token("your-token-here")

# Call endpoints
profile = api.accounts.get_current_user()
products = api.products.list()
```

## Zone Configuration

### Define Zones

```python
# settings.py
DJANGO_REVOLUTION = {
    'zones': {
        'public': {
            'apps': ['accounts', 'billing', 'payments'],
            'title': 'Public API',
            'description': 'API for public client applications',
            'public': True,
            'auth_required': False,
            'version': 'v1',
            'path_prefix': 'public'
        },
        'admin': {
            'apps': ['admin_panel', 'analytics'],
            'title': 'Admin API',
            'description': 'Administrative API endpoints',
            'public': False,
            'auth_required': True,
            'version': 'v1',
            'path_prefix': 'admin'
        }
    }
}
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

## DRF + Spectacular Configuration

### Quick Setup

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'My awesome API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
```

## URL Configuration

### Add Revolution URLs

```python
# urls.py
from django_revolution.urls_integration import add_revolution_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your existing URLs...
]

# Add Django Revolution URLs
urlpatterns = add_revolution_urls(urlpatterns)
```

### Generated URLs

Django Revolution automatically creates:

- `/api/{zone}/schema/` - Interactive Swagger UI
- `/api/{zone}/schema.yaml` - OpenAPI specification
- `/openapi/archive/` - Download generated clients

## Monorepo Integration

### Enable Monorepo Support

```python
# settings.py
DJANGO_REVOLUTION = {
    'zones': {
        # ... your zones
    },
    'monorepo': {
        'enabled': True,
        'project_root': BASE_DIR.parent,  # Path to monorepo root
        'packages_dir': 'packages',        # Where to sync clients
    }
}
```

### Generated Structure

```
monorepo/
├── packages/
│   ├── api-client/          # Generated TypeScript client
│   │   ├── package.json
│   │   └── src/
│   └── python-client/       # Generated Python client
│       ├── setup.py
│       └── src/
└── pnpm-workspace.yaml      # Auto-updated
```

## Advanced Usage

### Custom Templates

```python
# settings.py
DJANGO_REVOLUTION = {
    'templates': {
        'typescript': {
            'package_name': '@myorg/api-client',
            'package_version': '1.0.0',
        },
        'python': {
            'package_name': 'myorg-api-client',
            'package_version': '1.0.0',
        }
    }
}
```

### Archive Management

```bash
# Generate with archive
python manage.py revolution --archive

# List archives
python manage.py revolution --list-archives

# Download specific archive
python manage.py revolution --download-archive 2024-01-15_10-30-00
```

### Environment-Specific Configuration

```python
# settings.py
if DEBUG:
    DJANGO_REVOLUTION = {
        'zones': {
            'public': {
                'apps': ['accounts', 'billing'],
                'public': True,
            }
        }
    }
else:
    DJANGO_REVOLUTION = {
        'zones': {
            'public': {
                'apps': ['accounts', 'billing', 'payments'],
                'public': True,
            },
            'admin': {
                'apps': ['admin_panel'],
                'public': False,
                'auth_required': True,
            }
        }
    }
```

## Best Practices

1. **Run after changes**: Always run `python manage.py revolution` after modifying Django models or views
2. **Use zones**: Organize your API into logical zones for better structure
3. **Version control**: Commit generated clients to your repository
4. **CI/CD**: Add client generation to your deployment pipeline
5. **Testing**: Use generated clients in your tests for consistency

---

[← Back to Installation](installation.html) | [Next: CLI Reference →](cli.html)
