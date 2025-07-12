---
layout: default
title: API Reference
---

# API Reference

**Complete API documentation for Django Revolution.**

## Configuration

### DjangoRevolutionSettings

Main configuration class for Django Revolution.

```python
from django_revolution.config import DjangoRevolutionSettings

settings = DjangoRevolutionSettings(
    zones={
        'public': ZoneModel(
            apps=['accounts', 'billing'],
            title='Public API',
            description='Public endpoints',
            public=True,
            auth_required=False,
            version='v1',
            path_prefix='public'
        )
    },
    output_dir='openapi',
    auto_install_deps=True,
    typescript_enabled=True,
    python_enabled=True,
    archive_clients=True
)
```

### ZoneModel

Configuration for a single API zone.

```python
from django_revolution.config import ZoneModel

zone = ZoneModel(
    apps=['accounts', 'billing'],      # Django apps to include
    title='Public API',                # Human-readable title
    description='Public endpoints',    # Zone description
    public=True,                       # Is publicly accessible
    auth_required=False,               # Requires authentication
    version='v1',                      # API version
    path_prefix='public'               # URL path prefix
)
```

## Functions

### get_settings()

Get Django Revolution settings from Django settings.

```python
from django_revolution.config import get_settings

settings = get_settings()
print(settings.zones)
```

### add_revolution_urls()

Add Django Revolution URLs to your URL patterns.

```python
from django_revolution.urls_integration import add_revolution_urls

urlpatterns = [
    # Your existing URLs
]

urlpatterns = add_revolution_urls(urlpatterns)
```

### get_revolution_urlpatterns()

Get Django Revolution URL patterns.

```python
from django_revolution.urls_integration import get_revolution_urlpatterns

urlpatterns = [
    # Your existing URLs
    *get_revolution_urlpatterns()
]
```

### get_revolution_urls_info()

Get information about generated URLs.

```python
from django_revolution.urls_integration import get_revolution_urls_info

info = get_revolution_urls_info()
print(info['zones'])  # List of configured zones
print(info['schemas'])  # List of schema URLs
```

## Classes

### ZoneManager

Manages API zones and their configuration.

```python
from django_revolution.zones import ZoneManager

manager = ZoneManager()
zones = manager.get_zones()
```

### ZoneDetector

Automatically detects zones from Django apps.

```python
from django_revolution.zones import ZoneDetector

detector = ZoneDetector()
zones = detector.detect_zones()
```

### OpenAPIGenerator

Generates OpenAPI schemas and clients.

```python
from django_revolution.openapi import OpenAPIGenerator

generator = OpenAPIGenerator()
generator.generate()
```

## Management Commands

### revolution

Main Django management command for Django Revolution.

```bash
python manage.py revolution [options]
```

**Options:**

- `--zones`: Generate specific zones
- `--typescript`: Generate TypeScript only
- `--python`: Generate Python only
- `--archive`: Create archive
- `--monorepo`: Sync to monorepo
- `--no-monorepo`: Skip monorepo sync
- `--clean`: Clean output directory
- `--status`: Show status
- `--list-zones`: List zones
- `--install-deps`: Install dependencies
- `--check-deps`: Check dependencies
- `--list-archives`: List archives
- `--download-archive`: Download archive
- `--clean-archives`: Clean archives
- `--help`: Show help

## Templates

### Custom Templates

You can customize generated client templates:

```python
# settings.py
DJANGO_REVOLUTION = {
    'templates': {
        'typescript': {
            'package_name': '@myorg/api-client',
            'package_version': '1.0.0',
            'custom_template': 'path/to/template.ts.j2'
        },
        'python': {
            'package_name': 'myorg-api-client',
            'package_version': '1.0.0',
            'custom_template': 'path/to/template.py.j2'
        }
    }
}
```

## Utilities

### Logger

Django Revolution logger for debugging.

```python
from django_revolution.utils import Logger

logger = Logger()
logger.info("Generating clients...")
logger.error("Generation failed")
```

### ErrorHandler

Handles errors during client generation.

```python
from django_revolution.utils import ErrorHandler

handler = ErrorHandler()
try:
    # Generate clients
    pass
except Exception as e:
    handler.handle_error(e)
```

---

[← Back to CLI Reference](cli.html) | [Next: Architecture →](architecture.html)
