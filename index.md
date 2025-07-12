---
layout: default
title: Django Revolution
---

# Django Revolution

**Zone-based API Architecture for Django**

Install and go. Automatically generate TypeScript and Python clients from your Django API.

## Features

- 🚀 **Zone-based Architecture** - Organize your API endpoints into logical zones
- ⚡ **Auto Client Generation** - Generate TypeScript and Python clients automatically
- 🔧 **Django Integration** - Seamless integration with Django REST Framework
- 📦 **Monorepo Support** - Optional monorepo integration
- 🎯 **Simple Setup** - Just install, configure, and run
- 🛠️ **CLI Tools** - Powerful command-line tools

## Quick Start

```bash
# Install Django Revolution
pip install django-revolution

# Add to your Django settings
INSTALLED_APPS = [
    # ... your apps
    'django_revolution',
]

# Configure zones
DJANGO_REVOLUTION = {
    'zones': {
        'public': {
            'description': 'Public API endpoints',
            'urls': 'your_app.urls.public',
        },
        'private': {
            'description': 'Private API endpoints',
            'urls': 'your_app.urls.private',
        },
    }
}

# Add to your main urls.py
from django_revolution.urls_integration import add_revolution_urls

urlpatterns = [
    # ... your URLs
]

add_revolution_urls(urlpatterns)
```

## Generate Clients

```bash
# Generate OpenAPI schema and clients
python manage.py revolution

# This creates:
# - openapi/schema.yaml
# - clients/typescript/
# - clients/python/
```

## Documentation

- **[Installation](installation/)** - How to install and configure Django Revolution
- **[Usage](usage/)** - How to use zones and generate clients
- **[CLI Reference](cli/)** - Command-line interface documentation
- **[API Reference](api-reference/)** - Detailed API documentation
- **[Architecture](architecture/)** - Understanding zone-based architecture
- **[Troubleshooting](troubleshooting/)** - Common issues and solutions

## Examples

Check out our [sample project](https://github.com/markolofsen/django-revolution/tree/main/django_sample) for a complete working example.

## Support

- 🐛 [Issues](https://github.com/markolofsen/django-revolution/issues)
- 💬 [Discussions](https://github.com/markolofsen/django-revolution/discussions)

---

Made with ❤️ by [Unrealos](https://unrealos.com)
