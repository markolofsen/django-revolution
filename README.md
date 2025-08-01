# Django Revolution

> **Zero-config TypeScript & Python client generator for Django REST Framework** 🚀

[![PyPI version](https://badge.fury.io/py/django-revolution.svg)](https://badge.fury.io/py/django-revolution)
[![Python Support](https://img.shields.io/pypi/pyversions/django-revolution.svg)](https://pypi.org/project/django-revolution/)
[![Django Support](https://img.shields.io/pypi/djversions/django-revolution.svg)](https://pypi.org/project/django-revolution/)
[![License](https://img.shields.io/badge/license-Non--Commercial-red.svg)](LICENSE)

## ✨ What is Django Revolution?

**The fastest way to generate fully-authenticated TypeScript + Python clients from Django REST Framework.**

- 🧩 Organize your API into **zones** (`public`, `admin`, `mobile`, etc.)
- ⚙️ Generate strongly typed clients with **one command**
- 🔐 Built-in support for **Bearer tokens**, refresh logic, and API keys
- 🔄 Zero config for **Swagger/OpenAPI URLs**, **frontend integration**, and **monorepos**
- 🎯 **Optional monorepo integration** - works with or without monorepo structure
- 🚀 **Dynamic zone management** - no static files, everything generated in-memory
- 🎨 **Rich CLI interface** - interactive commands with beautiful output
- ⚡ **Multithreaded generation** - parallel processing for faster client generation
- 🧪 **Comprehensive testing** - full test suite with pytest
- 🔧 **Ready-to-use Pydantic configs** - type-safe configuration with IDE support

> No boilerplate. No manual sync. Just clean clients in seconds.

## 🧪 Example: Instantly Get a Typed API Client

```typescript
import API from '@myorg/api-client';

const api = new API('https://api.example.com');
api.setToken('your-access-token');

const profile = await api.public.getProfile();
const items = await api.public.listItems();
```

> 🔐 Auth, ⚙️ Headers, 🔄 Refresh – handled automatically.

## ⛔ Without Django Revolution

Manually update OpenAPI spec → Run generator → Fix broken types → Sync clients → Write token logic → Repeat on every change.

## ✅ With Django Revolution

One command. Done.

## 🚀 5-Minute Setup

### 1. Install

```bash
pip install django-revolution
```

### 2. Add to Django Settings

```python
# settings.py
INSTALLED_APPS = [
    'drf_spectacular',
    'django_revolution',  # Add this line
]
```

### 3. **Easy Configuration with Ready-to-Use Configs** 🎯

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

#### **Zone Configuration** (revolution.py)

```python
# api/settings/config/revolution.py
from django_revolution.app_config import (
    DjangoRevolutionConfig,
    ZoneConfig,
    MonorepoConfig,
    get_revolution_config
)

def create_revolution_config(env) -> Dict[str, Any]:
    """Get Django Revolution configuration as dictionary."""

    # Define zones with typed Pydantic models
    zones = {
        'public': ZoneConfig(
            apps=['accounts', 'billing', 'payments', 'support', 'public'],
            title='Public API',
            description='API for public client applications',
            public=True,
            auth_required=False,
            version='v1'
        ),
        'internal': ZoneConfig(
            apps=['system', 'mailer'],
            title='Internal API',
            description='Internal API for backend services',
            public=False,
            auth_required=True,
            version='v1'
        ),
        'admin': ZoneConfig(
            apps=['admin_panel', 'services'],
            title='Admin API',
            description='Administrative API endpoints',
            public=False,
            auth_required=True,
            version='v1'
        )
    }

    # Option 1: Without monorepo (simplest setup)
    project_root = env.root_dir
    return get_revolution_config(project_root=project_root, zones=zones, debug=env.debug)

    # Option 2: With monorepo integration
    # monorepo = MonorepoConfig(
    #     enabled=True,
    #     path=str(env.root_dir.parent / 'monorepo'),
    #     api_package_path='packages/api/src'
    # )
    # return get_revolution_config(project_root=project_root, zones=zones, debug=env.debug, monorepo=monorepo)
```

### 4. **Multithreaded Generation** ⚡

Django Revolution supports **multithreaded generation** for faster processing:

```python
# settings.py
DJANGO_REVOLUTION = {
    'enable_multithreading': True,  # Enable parallel processing
    'max_workers': 20,              # Maximum worker threads (default: 20)
    # ... other settings
}
```

**CLI Options:**
```bash
# Use 10 worker threads
python manage.py revolution --generate --max-workers 10

# Disable multithreading
python manage.py revolution --generate --no-multithreading
```

### 5. Generate Clients

```bash
# Generate everything (interactive mode)
python manage.py revolution

# Generate specific zones
python manage.py revolution --zones client admin

# TypeScript only
python manage.py revolution --typescript

# Without monorepo sync
python manage.py revolution --no-monorepo
```

## 🧬 What Does It Generate?

| Language       | Location                      | Structure                                                 |
| -------------- | ----------------------------- | --------------------------------------------------------- |
| **TypeScript** | `openapi/clients/typescript/` | `public/`, `admin/` → `index.ts`, `types.ts`, `services/` |
| **Python**     | `openapi/clients/python/`     | `public/`, `admin/` → `client.py`, `models/`, `setup.py`  |

💡 Each zone gets its own NPM/PyPI-style package. Ready to publish or import.

## ⚡️ TypeScript Client Auth & Usage

Django Revolution automatically generates a smart TypeScript API client with built-in authentication:

```typescript
import API from '@myorg/api-client';

const api = new API('https://api.example.com');

// Authentication
api.setToken('your-access-token', 'your-refresh-token');

// Call any endpoint
const user = await api.public.getCurrentUser();
const products = await api.public.listProducts();

// Check authentication status
if (api.isAuthenticated()) {
  // User is logged in
}
```

**Features included:**

- ✅ Automatic token management (localStorage)
- ✅ Custom headers support
- ✅ API key authentication
- ✅ Zone-based endpoint organization
- ✅ TypeScript types for all endpoints
- ✅ Error handling and validation

## 🌐 Auto-Generated URLs

Django Revolution **automatically generates** all necessary URLs for your API zones:

```python
# urls.py
from django_revolution import add_revolution_urls

urlpatterns = [
    # Your existing URLs
    path('admin/', admin.site.urls),
]

# Django Revolution automatically adds:
# - /schema/public/schema/ (OpenAPI spec)
# - /schema/public/schema/swagger/ (Swagger UI)
# - /schema/public/redoc/ (Redoc UI)
# - /schema/admin/schema/ (OpenAPI spec)
# - /schema/admin/schema/swagger/ (Swagger UI)
# - /schema/admin/redoc/ (Redoc UI)
# - /api/public/ (Public API endpoints)
# - /api/admin/ (Admin API endpoints)
# - /openapi/archive/ (Generated clients)
urlpatterns = add_revolution_urls(urlpatterns)
```

## 🧪 CLI Toolbox

### Django Management Commands

```bash
# Generate all clients (interactive mode)
python manage.py revolution

# Specific zones
python manage.py revolution --zones public admin

# Generator options
python manage.py revolution --typescript
python manage.py revolution --python
python manage.py revolution --no-archive

# Monorepo options
python manage.py revolution --no-monorepo

# Utility commands
python manage.py revolution --status
python manage.py revolution --list-zones
python manage.py revolution --validate
python manage.py revolution --clean

# New validation commands
python manage.py revolution --validate-zones
python manage.py revolution --show-urls
python manage.py revolution --test-schemas
```

### Standalone CLI (Interactive)

```bash
# Interactive CLI with rich interface
django-revolution

# Or run directly
python -m django_revolution.cli
```

## 🪆 Multi-Monorepo Integration (Optional)

Django Revolution supports **multiple monorepo configurations** with **pnpm**:

### With Multiple Monorepos

```python
# settings.py - With multiple monorepo configurations
from django_revolution.app_config import MonorepoConfig, MonorepoSettings

# Configure multiple monorepos
monorepo_settings = MonorepoSettings(
    enabled=True,
    configurations=[
        # Main frontend monorepo
        MonorepoConfig(
            name="frontend",
            enabled=True,
            path=str(BASE_DIR.parent / 'monorepo'),
            api_package_path='packages/api'
        ),
        # Mobile app monorepo
        MonorepoConfig(
            name="mobile",
            enabled=True,
            path=str(BASE_DIR.parent / 'mobile-monorepo'),
            api_package_path='packages/api-client'
        ),
        # Admin panel monorepo
        MonorepoConfig(
            name="admin",
            enabled=False,  # Disabled for now
            path=str(BASE_DIR.parent / 'admin-monorepo'),
            api_package_path='packages/admin-api'
        ),
    ]
)

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    monorepo=monorepo_settings
)
```

### With Single Monorepo

```python
# settings.py - With single monorepo (simplest)
from django_revolution.app_config import MonorepoConfig, MonorepoSettings

monorepo_settings = MonorepoSettings(
    enabled=True,
    configurations=[
        MonorepoConfig(
            name="frontend",
            enabled=True,
            path=str(BASE_DIR.parent / 'monorepo'),
            api_package_path='packages/api'
        ),
    ]
)

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    monorepo=monorepo_settings
)
```

### Without Monorepo

```python
# settings.py - Without monorepo (simplest)
DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones
)
```

**Auto-generated monorepo structure:**

```yaml
# pnpm-workspace.yaml (auto-generated)
packages:
  - 'packages/**'
  - 'packages/api/**' # Added automatically
```

**Package.json dependencies:**

```json
{
  "dependencies": {
    "@markolofsen/public-api-client": "workspace:*",
    "@markolofsen/admin-api-client": "workspace:*"
  }
}
```

**Generated locally:**

- `openapi/clients/typescript/` - TypeScript clients
- `openapi/clients/python/` - Python clients
- `openapi/archive/` - Versioned archives

## 🔧 Configuration

### **Easy Configuration with Ready-to-Use Configs** 🎯

Django Revolution provides **pre-built Pydantic configurations** that eliminate manual setup:

#### **1. DRF + Spectacular Configuration**

```python
# api/settings/config/services.py
from django_revolution.drf_config import create_drf_config

# One function call - everything configured!
drf_config = create_drf_config(
    title="My API",
    description="My awesome API",
    version="1.0.0",
    schema_path_prefix="/apix/",
    enable_browsable_api=False,
    enable_throttling=True,
)

# Get Django settings
settings = drf_config.get_django_settings()
REST_FRAMEWORK = settings['REST_FRAMEWORK']
SPECTACULAR_SETTINGS = settings['SPECTACULAR_SETTINGS']
```

#### **2. Zone Configuration**

```python
# api/settings/config/revolution.py
from django_revolution.app_config import ZoneConfig, get_revolution_config

# Typed zone definitions with Pydantic models
zones = {
    'public': ZoneConfig(
        apps=['accounts', 'billing', 'payments'],
        title='Public API',
        description='API for public client applications',
        public=True,
        auth_required=False,
        version='v1'
    ),
    'admin': ZoneConfig(
        apps=['admin_panel', 'analytics'],
        title='Admin API',
        description='Administrative API endpoints',
        public=False,
        auth_required=True,
        version='v1'
    )
}

# Option 1: Without monorepo (simplest)
config = get_revolution_config(project_root=Path.cwd(), zones=zones)

# Option 2: With single monorepo
from django_revolution.app_config import MonorepoConfig, MonorepoSettings
monorepo_settings = MonorepoSettings(
    enabled=True,
    configurations=[
        MonorepoConfig(
            name="frontend",
            enabled=True,
            path=str(Path.cwd().parent / 'monorepo'),
            api_package_path='packages/api'
        ),
    ]
)
config = get_revolution_config(project_root=Path.cwd(), zones=zones, monorepo=monorepo_settings)

# Option 3: With multiple monorepos
monorepo_settings = MonorepoSettings(
    enabled=True,
    configurations=[
        MonorepoConfig(name="frontend", enabled=True, path=str(Path.cwd().parent / 'monorepo'), api_package_path='packages/api'),
        MonorepoConfig(name="mobile", enabled=True, path=str(Path.cwd().parent / 'mobile-monorepo'), api_package_path='packages/api-client'),
        MonorepoConfig(name="admin", enabled=False, path=str(Path.cwd().parent / 'admin-monorepo'), api_package_path='packages/admin-api'),
    ]
)
config = get_revolution_config(project_root=Path.cwd(), zones=zones, monorepo=monorepo_settings)
```

## ✅ When to Use

### ✅ Perfect For

- **Large Django projects** with multiple API audiences
- **Monorepo architectures** with frontend/backend separation
- **Teams** needing consistent API client generation
- **Projects** requiring zone-based API organization
- **Automated CI/CD** pipelines
- **Simple projects** without monorepo (optional integration)

### ❌ Not For

- **Simple single-zone APIs** (overkill)
- **Non-Django projects** (use Fern.dev instead)
- **Manual control freaks** (use drf-spectacular + generators)

## 🧠 Power Features

### Dynamic Zone Management

**No more static files!** Django Revolution uses **in-memory dynamic module generation**:

- ✅ **Zero static files** - Everything generated dynamically
- ✅ **Zone caching** - Fast repeated generation
- ✅ **Module registry** - Automatic cleanup and management
- ✅ **URL pattern validation** - Real-time validation
- ✅ **Schema testing** - Test generation before production

### Archive Management

```bash
# Automatic versioning with timestamped archives
openapi/archive/
├── files/
│   ├── 2024-01-15_14-30-00/
│   │   ├── public.zip
│   │   └── admin.zip
│   └── 2024-01-15_15-45-00/
│       ├── public.zip
│       └── admin.zip
└── latest/
    ├── public.zip
    └── admin.zip
```

Each archive contains both TypeScript and Python clients:

- `typescript/` - Generated TypeScript client
- `python/` - Generated Python client

### Custom Templates

```python
'generators': {
    'typescript': {
        'custom_templates': './templates/typescript'
    },
    'python': {
        'custom_templates': './templates/python'
    }
}
```

### Programmatic Usage

```python
from django_revolution import OpenAPIGenerator, get_settings

config = get_settings()
generator = OpenAPIGenerator(config)
summary = generator.generate_all(zones=['public', 'admin'])
```

## 📊 Comparison Table

| Feature                           | Django Revolution  | drf-spectacular + generators | openapi-generator-cli | Fern.dev | Manual Setup |
| --------------------------------- | ------------------ | ---------------------------- | --------------------- | -------- | ------------ |
| **Zone-based architecture**       | ✅ **UNIQUE**      | ❌                           | ❌                    | ✅       | ❌           |
| **Dynamic zone management**       | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Automatic URL generation**      | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Monorepo integration**          | ✅ **OPTIONAL**    | ❌                           | ❌                    | ✅       | ❌           |
| **Django management commands**    | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Rich CLI interface**            | ✅ **UNIQUE**      | ❌                           | ❌                    | ✅       | ❌           |
| **Zone validation & testing**     | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Archive management**            | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **TypeScript + Python clients**   | ✅                 | ✅                           | ✅                    | ✅       | ✅           |
| **DRF native integration**        | ✅ **SEAMLESS**    | ✅                           | ⚠️ (via schema)       | ❌       | ✅           |
| **Ready-to-use Pydantic configs** | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Zero configuration**            | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Environment variables**         | ✅ **Pydantic**    | ❌                           | ❌                    | ❌       | ❌           |
| **CLI interface**                 | ✅ **Rich output** | ❌                           | ✅                    | ✅       | ❌           |
| **Multithreaded generation**      | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |
| **Comprehensive testing**         | ✅ **UNIQUE**      | ❌                           | ❌                    | ❌       | ❌           |

## 🙋 FAQ

**Q: Is this production-ready?**  
✅ Yes. Used in monorepos and multi-tenant production apps.

**Q: What if I use DRF with custom auth?**  
Use `setHeaders()` or `setApiKey()` to inject custom logic.

**Q: Can I use this in non-monorepo setups?**  
Absolutely! Monorepo integration is completely optional. Just don't pass the `monorepo` parameter to `get_revolution_config()`.

**Q: How do I configure multiple monorepos?**  
Use `MonorepoSettings` with a list of `MonorepoConfig` objects. Each config can be enabled/disabled independently.

**Q: What if I need only TypeScript clients?**  
Use `--typescript` flag to generate only TS clients.

**Q: Does it support custom OpenAPI decorators?**  
Yes, built on `drf-spectacular` so all extensions apply.

**Q: How do I use the ready-to-use Pydantic configs?**  
Simply import and use: `from django_revolution.drf_config import create_drf_config` and `from django_revolution.app_config import ZoneConfig, get_revolution_config`.

**Q: Are the Pydantic configs type-safe?**  
Yes! Full Pydantic v2 validation with IDE autocomplete and error checking.

**Q: How do I disable monorepo integration?**  
Either don't pass the `monorepo` parameter to `get_revolution_config()`, or use the `--no-monorepo` flag when running the command.

**Q: What's new in the latest version?**  
- 🚀 **Dynamic zone management** - No more static files, everything generated in-memory
- 🎨 **Rich CLI interface** - Beautiful interactive commands with progress tracking
- ✅ **Zone validation & testing** - Validate zones and test schema generation
- 🔧 **Unified CLI architecture** - Single codebase for Django commands and standalone CLI
- 📊 **Enhanced output** - Rich tables and progress indicators
- ⚡ **Multithreaded generation** - Parallel processing for faster client generation
- 🧪 **Comprehensive testing** - Full test suite with pytest and proper mocking
- 📦 **Multi-monorepo support** - Support for multiple monorepo configurations
- 🔧 **pnpm-only integration** - Simplified package manager support

**Q: How does the dynamic zone system work?**  
Django Revolution creates URL configuration modules in-memory using Python's `importlib` and `exec`. This eliminates the need for static `.py` files and provides better performance and flexibility.

**Q: How does multithreading improve performance?**  
Multithreading allows parallel processing of multiple zones, schema generation, and client generation. For 3 zones, you can see 2-3x speedup compared to sequential processing.

**Q: Why only pnpm support?**  
We focus on pnpm for its superior monorepo support, faster installation, and better workspace management. This simplifies the codebase and provides a consistent experience.

**Q: How do I manage multiple monorepo configurations?**  
Use `MonorepoSettings` with a list of `MonorepoConfig` objects. Each configuration can be enabled/disabled independently, and clients are synced to all enabled configurations.

## 🤝 Contributing

```bash
# Development setup
git clone https://github.com/markolofsen/django-revolution.git
cd django-revolution
pip install -e ".[dev]"

# Run tests
pytest
black django_revolution/
isort django_revolution/
```

## 📞 Support

- **Documentation**: [https://revolution.unrealos.com/](https://revolution.unrealos.com/)
- **Issues**: [https://github.com/markolofsen/django-revolution/issues](https://github.com/markolofsen/django-revolution/issues)
- **Discussions**: [https://github.com/markolofsen/django-revolution/discussions](https://github.com/markolofsen/django-revolution/discussions)

## 📝 License

Non-Commercial License - see [LICENSE](LICENSE) file for details.

For commercial use, please contact Unrealos Inc. at licensing@unrealos.com

---

**Made with ❤️ by the [Unrealos Team](https://unrealos.com)**

**Django Revolution** - The **ONLY** tool that makes Django API client generation **truly automated** and **zone-aware**.
