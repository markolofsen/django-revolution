---
layout: default
title: API Reference
---

# API Reference

**Complete API documentation for Django Revolution.**

## 🎯 Configuration

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

### ZoneConfig (Pydantic Model)

Type-safe zone configuration using Pydantic.

```python
from django_revolution.app_config import ZoneConfig

zone = ZoneConfig(
    apps=['accounts', 'billing'],      # Django apps to include
    title='Public API',                # Human-readable title
    description='Public endpoints',    # Zone description
    public=True,                       # Is publicly accessible
    auth_required=False,               # Requires authentication
    version='v1',                      # API version
    path_prefix='public'               # URL path prefix
)
```

## 🔧 Core Functions

### get_settings()

Get Django Revolution settings from Django settings.

```python
from django_revolution.config import get_settings

settings = get_settings()
print(settings.zones)
```

### get_revolution_config()

Get Django Revolution configuration with Pydantic models.

```python
from django_revolution.app_config import get_revolution_config

config = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    debug=DEBUG,
    monorepo=monorepo_config
)
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

urls_info = get_revolution_urls_info()
for zone, info in urls_info.items():
    print(f"Zone: {zone}")
    print(f"  Schema URL: {info['schema_url']}")
    print(f"  API URL: {info['api_url']}")
```

## 🚀 Dynamic Zone Management

### DynamicZoneManager

Manages zone configuration and URL generation in-memory.

```python
from django_revolution.zones import DynamicZoneManager

zone_manager = DynamicZoneManager()

# Create dynamic URL configuration module
urlconf_module = zone_manager.create_dynamic_urlconf_module('public', zone_config)

# Detect apps in zone
apps = zone_manager.detect_apps_in_zone(zone_config)

# Validate zone configuration
is_valid = zone_manager.validate_zone_configuration('public', zone_config)
```

### DynamicZoneDetector

Detects Django apps and their URL patterns.

```python
from django_revolution.zones import DynamicZoneDetector

detector = DynamicZoneDetector()

# Detect apps in project
apps = detector.detect_apps()

# Get URL patterns for app
patterns = detector.get_app_url_patterns('accounts')

# Validate app exists
exists = detector.app_exists('accounts')
```

## 📦 OpenAPI Generation

### OpenAPIGenerator

Generates OpenAPI schemas and client libraries.

```python
from django_revolution.openapi.generator import OpenAPIGenerator

generator = OpenAPIGenerator(config)

# Generate schemas for all zones
schemas = generator.generate_schemas()

# Generate TypeScript client
ts_client = generator.generate_typescript_client()

# Generate Python client
py_client = generator.generate_python_client()

# Generate archive
archive = generator.generate_archive()
```

### ArchiveManager

Manages client archives.

```python
from django_revolution.openapi.archive_manager import ArchiveManager

archive_manager = ArchiveManager(output_dir)

# Create archive
archive_path = archive_manager.create_archive()

# List archives
archives = archive_manager.list_archives()

# Download archive
archive_manager.download_archive('2024-01-15_10-30-00')
```

## 🛠️ Development Tools

### VersionManager

Manages version across all package files.

```python
from scripts.version_manager import VersionManager

version_manager = VersionManager()

# Get current version
version = version_manager.get_current_version()

# Bump version
new_version = version_manager.bump_version('patch')

# Validate version consistency
is_consistent = version_manager.validate_version_consistency()

# Regenerate requirements
version_manager.regenerate_requirements()
```

### Publisher

Interactive package publishing.

```python
from scripts.publisher import main as publish

# Interactive publishing
exit_code = publish()
```

## 🎨 CLI Components

### CLI Main Function

Main CLI entry point.

```python
from django_revolution.cli import main

# Run CLI
exit_code = main()
```

### Development CLI

Interactive development interface.

```python
from scripts.dev_cli import main as dev_cli

# Run development CLI
dev_cli()
```

## 🔧 DRF Configuration

### create_drf_config()

Create DRF and Spectacular configuration.

```python
from django_revolution.drf_config import create_drf_config

drf_config = create_drf_config(
    title='My API',
    description='My awesome API',
    version='1.0.0',
    schema_path_prefix='/apix/',
    enable_browsable_api=False,
    enable_throttling=False
)

# Get REST framework settings
rest_framework_settings = drf_config.get_rest_framework_settings()

# Get Spectacular settings
spectacular_settings = drf_config.get_spectacular_settings()

# Get all Django settings
django_settings = drf_config.get_django_settings()
```

## 📋 Utility Functions

### auto_install_dependencies()

Automatically install required dependencies.

```python
from django_revolution.utils import auto_install_dependencies

success = auto_install_dependencies()
if success:
    print("✅ Dependencies installed")
else:
    print("❌ Failed to install dependencies")
```

### run_command()

Run shell commands with logging.

```python
from django_revolution.utils import run_command

success, output = run_command("npm install @hey-api/openapi-ts")
if success:
    print(f"✅ Command succeeded: {output}")
else:
    print(f"❌ Command failed: {output}")
```

### ensure_directories()

Ensure directories exist.

```python
from django_revolution.utils import ensure_directories
from pathlib import Path

success = ensure_directories(
    Path("openapi/schemas"),
    Path("clients/typescript"),
    Path("clients/python")
)
```

### render_template()

Render Jinja2 templates.

```python
from django_revolution.utils import render_template

template = "Hello {{ name }}!"
context = {"name": "World"}
result = render_template(template, context)
# Result: "Hello World!"
```

## 🔍 Validation Functions

### validate_zone_configuration()

Validate zone configuration.

```python
from django_revolution.zones import validate_zone_configuration

is_valid = validate_zone_configuration('public', zone_config)
if not is_valid:
    print("❌ Invalid zone configuration")
```

### validate_environment()

Validate Django Revolution environment.

```python
from django_revolution.utils import validate_environment

validation_result = validate_environment()
if validation_result['success']:
    print("✅ Environment is valid")
else:
    print(f"❌ Environment issues: {validation_result['errors']}")
```

## 📊 Data Models

### GenerationResult

Result of client generation.

```python
from django_revolution.openapi.generator import GenerationResult

result = GenerationResult(
    success=True,
    schemas={'public': Path('openapi/schemas/public.yaml')},
    typescript_client=Path('clients/typescript/index.ts'),
    python_client=Path('clients/python/client.py'),
    archive=Path('openapi/archive/2024-01-15_10-30-00.zip'),
    errors=[],
    warnings=[]
)
```

### ZoneInfo

Information about a zone.

```python
from django_revolution.zones import ZoneInfo

zone_info = ZoneInfo(
    name='public',
    apps=['accounts', 'billing'],
    url_patterns=5,
    schema_patterns=3,
    is_valid=True,
    errors=[],
    warnings=[]
)
```

## 🎯 Error Handling

### ErrorHandler

Comprehensive error handling and validation.

```python
from django_revolution.utils import ErrorHandler

error_handler = ErrorHandler()

# Handle exception
result = error_handler.handle_exception(
    exception,
    context="zone generation"
)

# Validate path
is_valid = error_handler.validate_path(Path("openapi/schemas"))

# Validate file
is_valid = error_handler.validate_file(Path("settings.py"))
```

## 📝 Logging

### Logger

Enhanced logger with rich output.

```python
from django_revolution.utils import Logger

logger = Logger("my_module")

logger.info("Starting generation...")
logger.success("Generation completed!")
logger.warning("Some warnings occurred")
logger.error("Generation failed")
logger.debug("Debug information")
```

## 🔧 Configuration Examples

### Basic Configuration

```python
# settings.py
from django_revolution.app_config import ZoneConfig, get_revolution_config

zones = {
    'public': ZoneConfig(
        apps=['accounts', 'billing'],
        title='Public API',
        description='Public endpoints',
        public=True,
        auth_required=False
    )
}

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones
)
```

### Advanced Configuration

```python
# settings.py
from django_revolution.app_config import ZoneConfig, MonorepoConfig, get_revolution_config

zones = {
    'public': ZoneConfig(
        apps=['accounts', 'billing', 'payments'],
        title='Public API',
        description='Public endpoints',
        public=True,
        auth_required=False,
        version='v1',
        path_prefix='public'
    ),
    'admin': ZoneConfig(
        apps=['admin_panel', 'analytics'],
        title='Admin API',
        description='Administrative endpoints',
        public=False,
        auth_required=True,
        version='v1',
        path_prefix='admin'
    )
}

monorepo = MonorepoConfig(
    enabled=True,
    path=str(BASE_DIR.parent.parent / 'monorepo'),
    api_package_path='packages/api/src'
)

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    monorepo=monorepo,
    debug=DEBUG,
    output_config={
        'base_directory': 'custom_openapi',
        'typescript': {
            'enabled': True,
            'package_name': '@myorg/custom-api'
        },
        'python': {
            'enabled': True,
            'package_name': 'myorg_custom_api'
        }
    }
)
```

---

[← Back to CLI Reference](cli.html) | [Next: Architecture →](architecture.html)
