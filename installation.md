---
layout: default
title: Installation
---

# Installation Guide

**Get Django Revolution running in 2 minutes.**

## 🚀 Quick Install

```bash
# Using pip
pip install django-revolution

# Using poetry
poetry add django-revolution

# Using requirements.txt
echo "django-revolution>=1.0.11" >> requirements.txt
pip install -r requirements.txt
```

### Add to Django

```python
# settings.py
INSTALLED_APPS = [
    'django_revolution',
    # your existing apps
]
```

### Test Installation

```bash
# Check status
python manage.py revolution --status

# Or use standalone CLI
django-revolution --status
```

**Done!** Django Revolution auto-installs dependencies when first used.

## ✅ Verify Installation

### Check Version & Status

```bash
# Django management command
python manage.py revolution --status

# Standalone CLI
django-revolution --status

# Development CLI
python scripts/dev_cli.py
```

### List Available Commands

```bash
# Django management command
python manage.py revolution --help

# Standalone CLI
django-revolution --help

# Development tools
python scripts/dev_cli.py
```

### Install Dependencies

```bash
# Auto-install dependencies
python manage.py revolution --install-deps

# Or manually
pip install -r requirements-dev.txt
```

### List Zones

```bash
python manage.py revolution --list-zones
```

## 📦 Auto-Installed Dependencies

**Automatically installed when needed:**

- `@hey-api/openapi-ts` - TypeScript client generation
- `datamodel-code-generator` - Python client generation
- `drf-spectacular` - OpenAPI schema generation

**Pre-installed with package:**

- `Django>=3.2` - Web framework
- `djangorestframework>=3.12.0` - API framework
- `drf-spectacular>=0.24.0` - OpenAPI schema generation
- `Jinja2>=3.0.0` - Template engine
- `PyYAML>=6.0` - YAML processing
- `pydantic>=2.0.0` - Data validation
- `pydantic-settings>=2.0.0` - Settings management
- `questionary>=2.0.0` - Interactive CLI
- `rich>=13.0.0` - Rich terminal output
- `datamodel-code-generator>=0.31.0` - Python client generation
- `django-filter>=22.0.0` - Filtering support
- `djangorestframework-simplejwt>=5.0.0` - JWT authentication

## 🛠️ Development Installation

### From Source

```bash
# Clone repository
git clone https://github.com/markolofsen/django-revolution.git
cd django-revolution

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Test installation
python scripts/dev_cli.py
```

### With Poetry

```bash
# Add to project
poetry add django-revolution

# Add development dependencies
poetry add --group dev django-revolution[dev]
```

### With Requirements Files

```bash
# Main dependencies
pip install -r requirements.txt

# Development dependencies
pip install -r requirements-dev.txt

# Minimal dependencies (core only)
pip install -r requirements-minimal.txt
```

## 🔧 Development Tools

After installation, you have access to:

```bash
# Interactive development CLI
python scripts/dev_cli.py

# Version management
python scripts/version_manager.py get
python scripts/version_manager.py bump --bump-type patch

# Generate requirements files
python scripts/generate_requirements.py

# Interactive publishing
python scripts/publisher.py

# Test generation
./scripts/test_generation.sh
```

### Package Commands (after installation)

```bash
# Install in development mode
pip install -e .

# Use package commands
django-revolution --help
version-manager --help
publisher --help
dev-cli --help
generate-requirements
```

## 🚨 Troubleshooting

### Node.js Not Found

Django Revolution auto-installs npm packages but requires Node.js:

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS with Homebrew
brew install node

# Windows with Chocolatey
choco install nodejs
```

### Permission Errors

```bash
# Fix npm permissions (Linux/macOS)
sudo chown -R $(whoami) ~/.npm

# Make scripts executable
chmod +x scripts/*.py scripts/*.sh
```

### Import Errors

```bash
# Check installation
python -c "import django_revolution; print('✅ Django Revolution installed')"

# Check scripts
python -c "from scripts.version_manager import VersionManager; print('✅ Scripts available')"

# Reinstall if needed
pip uninstall django-revolution
pip install django-revolution
```

### TOML Parsing Issues

```bash
# Install toml package
pip install toml

# Or install development dependencies
pip install -r requirements-dev.txt
```

### Generation Fails

```bash
# Check detailed status
python manage.py revolution --status

# Validate zones
python manage.py revolution --validate-zones

# Test schema generation
python manage.py revolution --test-schemas

# Install dependencies manually
python manage.py revolution --install-deps

# Clean and retry
python manage.py revolution --clean
python manage.py revolution
```

## ⚙️ Configuration

### Basic Django Settings

```python
# settings.py
from django_revolution.app_config import ZoneConfig, get_revolution_config

# Define zones
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

# Configure Django Revolution
DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    debug=DEBUG
)
```

### Optional Settings

```python
# settings.py (optional customization)
DJANGO_REVOLUTION = {
    'output_dir': 'openapi',           # Default: 'openapi'
    'auto_install_deps': True,         # Default: True
    'typescript_enabled': True,        # Default: True
    'python_enabled': True,            # Default: True
    'archive_clients': True,           # Default: True
    'monorepo': {                      # Optional monorepo config
        'enabled': False,
        'path': '/path/to/monorepo',
        'api_package_path': 'packages/api/src'
    }
}
```

### Environment Variables

```bash
# Skip auto-installation of dependencies
export DJANGO_REVOLUTION_NO_AUTO_INSTALL=1

# Custom output directory
export DJANGO_REVOLUTION_OUTPUT_DIR=/custom/path

# Debug mode
export DJANGO_REVOLUTION_DEBUG=1
```

## 📋 System Requirements

### Minimum Requirements

- Python 3.9+
- Django 3.2+
- 100MB free disk space
- Internet connection (for dependency installation)

### Recommended

- Python 3.11+
- Django 4.2+
- Node.js 18+ (for TypeScript generation)
- Poetry (for dependency management)

### Development Requirements

- Git
- Make (optional, for development scripts)
- Virtual environment (recommended)

---

[← Back to Home](index.html) | [Next: Usage →](usage.html)
