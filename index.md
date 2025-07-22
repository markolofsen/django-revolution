---
layout: default
title: Django Revolution
---

# Django Revolution

**Zero-config TypeScript & Python client generator for Django REST Framework** 🚀

Install and go. Automatically generate fully-authenticated TypeScript and Python clients from your Django API.

## ✨ Features

- 🧩 **Zone-based Architecture** - Organize your API endpoints into logical zones
- ⚡ **Auto Client Generation** - Generate TypeScript and Python clients automatically
- 🔐 **Built-in Authentication** - Bearer tokens, refresh logic, and API keys
- 🔄 **Zero Config** - Works with Swagger/OpenAPI URLs and frontend integration
- 🚀 **Dynamic Zone Management** - No static files, everything generated in-memory
- 🎨 **Rich CLI Interface** - Interactive commands with beautiful output
- 📦 **Monorepo Support** - Optional monorepo integration
- 🛠️ **Development Tools** - Comprehensive CLI toolbox for development

## 🚀 Quick Start

```bash
# Install Django Revolution
pip install django-revolution

# Add to your Django settings
INSTALLED_APPS = [
    # ... your apps
    'django_revolution',
]

# Configure zones with Pydantic models
from django_revolution.app_config import ZoneConfig, get_revolution_config

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
        apps=['admin_panel', 'services'],
        title='Admin API',
        description='Administrative API endpoints',
        public=False,
        auth_required=True,
        version='v1',
        path_prefix='admin'
    )
}

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones
)

# Add to your main urls.py
from django_revolution.urls_integration import add_revolution_urls

urlpatterns = [
    # ... your URLs
]

add_revolution_urls(urlpatterns)
```

## 🎯 Generate Clients

```bash
# Interactive generation (recommended)
python manage.py revolution

# Direct generation
python manage.py revolution --zones public,admin --typescript --python

# This creates:
# - openapi/schemas/{zone}.yaml
# - clients/typescript/
# - clients/python/
# - openapi/archive/
```

## 🛠️ Development Tools

```bash
# Interactive development CLI
python scripts/dev_cli.py

# Version management
python scripts/version_manager.py bump --bump-type patch

# Generate requirements files
python scripts/generate_requirements.py

# Interactive publishing
python scripts/publisher.py
```

## 📚 Documentation

- **[Installation](installation/)** - How to install and configure Django Revolution
- **[Usage](usage/)** - How to use zones and generate clients
- **[CLI Reference](cli/)** - Command-line interface documentation
- **[API Reference](api-reference/)** - Detailed API documentation
- **[Architecture](architecture/)** - Understanding zone-based architecture
- **[Troubleshooting](troubleshooting/)** - Common issues and solutions

## 🧪 Examples

Check out our [sample project](https://github.com/markolofsen/django-revolution/tree/main/django_sample) for a complete working example.

## 🎯 Ready-to-Use Clients

```typescript
import API from '@myorg/api-client';

const api = new API('https://api.example.com');
api.setToken('your-access-token');

const profile = await api.public.getProfile();
const items = await api.public.listItems();
```

> 🔐 Auth, ⚙️ Headers, 🔄 Refresh – handled automatically.

## 🆕 What's New

- **Dynamic Zone Management** - No more static zone files
- **Rich CLI Interface** - Beautiful interactive commands
- **Development Scripts** - Comprehensive development toolbox
- **Requirements Generation** - Automatic requirements.txt creation
- **Version Management** - Automated version bumping and validation

## Support

- 🐛 [Issues](https://github.com/markolofsen/django-revolution/issues)
- 💬 [Discussions](https://github.com/markolofsen/django-revolution/discussions)

---

Made with ❤️ by [Unrealos](https://unrealos.com)
