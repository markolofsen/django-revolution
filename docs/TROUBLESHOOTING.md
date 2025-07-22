---
layout: default
title: Troubleshooting
---

# Troubleshooting

**Common issues and solutions for Django Revolution.**

## 🚨 Installation Issues

### ImportError: No module named 'django_revolution'

**Problem**: Django Revolution is not installed or not in Python path.

**Solution**:

```bash
# Install Django Revolution
pip install django-revolution

# Verify installation
python -c "import django_revolution; print('✅ Installed')"

# Check version
python -c "import django_revolution; print(django_revolution.__version__)"
```

### ModuleNotFoundError: No module named 'django_filters'

**Problem**: Missing dependencies.

**Solution**:

```bash
# Install missing dependencies
pip install django-filter djangorestframework-simplejwt

# Or let Django Revolution install them
python manage.py revolution --install-deps

# Or install from requirements
pip install -r requirements.txt
```

### TOML Parsing Issues

**Problem**: `ModuleNotFoundError: No module named 'toml'` or `tomllib`.

**Solution**:

```bash
# Install toml package
pip install toml

# Or install development dependencies
pip install -r requirements-dev.txt

# The script automatically handles both tomllib (Python 3.11+) and toml package
```

## ⚙️ Configuration Issues

### Zone Configuration Error

**Problem**: Invalid zone configuration in settings.

**Solution**:

```python
# settings.py - Correct format with Pydantic models
from django_revolution.app_config import ZoneConfig, get_revolution_config

zones = {
    'public': ZoneConfig(
        apps=['accounts', 'billing'],  # List of apps
        title='Public API',
        description='Public endpoints',
        public=True,
        auth_required=False,
        version='v1',
        path_prefix='public'
    )
}

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones
)
```

### URL Integration Error

**Problem**: URLs not properly integrated.

**Solution**:

```python
# urls.py - Correct integration
from django_revolution.urls_integration import add_revolution_urls

urlpatterns = [
    # Your existing URLs
]

# Add Django Revolution URLs
urlpatterns = add_revolution_urls(urlpatterns)
```

## 🔧 Generation Issues

### Command Not Found: revolution

**Problem**: Django management command not recognized.

**Solution**:

```bash
# Check if app is in INSTALLED_APPS
python manage.py check

# Verify command exists
python manage.py help | grep revolution

# Reinstall if needed
pip uninstall django-revolution
pip install django-revolution

# Or use standalone CLI
django-revolution --help
```

### Zone Validation Failures

**Problem**: Zones fail validation during generation.

**Solution**:

```bash
# Validate zones with detailed output
python manage.py revolution --validate-zones

# Check specific zone
python manage.py revolution --show-urls

# Test schema generation
python manage.py revolution --test-schemas

# Check status
python manage.py revolution --status
```

### Schema Generation Errors

**Problem**: OpenAPI schema generation fails.

**Solution**:

```bash
# Test schema generation
python manage.py revolution --test-schemas

# Check drf-spectacular installation
pip install drf-spectacular

# Verify Django settings
python manage.py check

# Clean and retry
python manage.py revolution --clean
python manage.py revolution
```

## 🛠️ Development Scripts Issues

### Script Permission Errors

**Problem**: Scripts are not executable.

**Solution**:

```bash
# Make scripts executable
chmod +x scripts/*.py scripts/*.sh

# Or run with python
python scripts/dev_cli.py
python scripts/version_manager.py get
```

### Import Errors in Scripts

**Problem**: `ImportError: attempted relative import with no known parent package`.

**Solution**:

```bash
# Run from correct directory
cd /path/to/django_revolution
python scripts/dev_cli.py

# Or install in development mode
pip install -e .

# Use package commands
dev-cli
version-manager get
```

### Version Management Issues

**Problem**: Version bumping or validation fails.

**Solution**:

```bash
# Check current version
python scripts/version_manager.py get

# Validate version consistency
python scripts/version_manager.py validate

# Bump version with specific type
python scripts/version_manager.py bump --bump-type patch

# Regenerate requirements after version bump
python scripts/version_manager.py requirements
```

## 📦 Publishing Issues

### Build Failures

**Problem**: Package build fails during publishing.

**Solution**:

```bash
# Clean old builds
rm -rf build/ dist/ *.egg-info/

# Install build dependencies
pip install build twine

# Build manually
python -m build

# Check build artifacts
ls -la dist/
```

### PyPI Upload Errors

**Problem**: Upload to PyPI fails.

**Solution**:

```bash
# Use interactive publisher
python scripts/publisher.py

# Check credentials
python -m twine check dist/*

# Test upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Then upload to PyPI
python -m twine upload dist/*
```

## 🔍 Debugging

### Enable Debug Mode

```bash
# Set debug environment variable
export DJANGO_REVOLUTION_DEBUG=1

# Run with debug output
python manage.py revolution --debug

# Check logs
python manage.py revolution --status
```

### Check Dependencies

```bash
# Check all dependencies
python manage.py revolution --check-deps

# Install missing dependencies
python manage.py revolution --install-deps

# Verify Node.js installation
node --version
npm --version
```

### Validate Environment

```bash
# Validate entire environment
python manage.py revolution --validate

# Check Django setup
python manage.py check

# Verify zone configuration
python manage.py revolution --validate-zones
```

## 🚀 Performance Issues

### Slow Generation

**Problem**: Client generation takes too long.

**Solution**:

```bash
# Generate specific zones only
python manage.py revolution --zones public

# Skip archive creation
python manage.py revolution --no-archive

# Use development mode for faster iteration
export DJANGO_REVOLUTION_DEBUG=1
```

### Memory Issues

**Problem**: High memory usage during generation.

**Solution**:

```bash
# Clean up old modules
python manage.py revolution --clean

# Generate zones one by one
python manage.py revolution --zones public
python manage.py revolution --zones admin

# Monitor memory usage
python manage.py revolution --status
```

## 🔧 CLI Issues

### Interactive CLI Problems

**Problem**: Interactive CLI doesn't work properly.

**Solution**:

```bash
# Check questionary installation
pip install questionary

# Use command line mode instead
python manage.py revolution --zones public --typescript

# Or use standalone CLI
django-revolution --zones public --typescript
```

### Rich Output Issues

**Problem**: Terminal output is not formatted properly.

**Solution**:

```bash
# Check rich installation
pip install rich

# Use plain output
export DJANGO_REVOLUTION_NO_RICH=1
python manage.py revolution --status

# Or use simple output
python manage.py revolution --status --no-color
```

## 📋 Common Error Messages

### "Zone 'public' not found"

**Solution**: Check zone configuration in settings.py

### "No apps found for zone 'public'"

**Solution**: Verify app names in zone configuration

### "Schema generation failed"

**Solution**: Check drf-spectacular configuration

### "Client generation failed"

**Solution**: Verify Node.js and npm installation

### "Monorepo sync failed"

**Solution**: Check monorepo configuration and permissions

## 🆘 Getting Help

### Self-Diagnosis

```bash
# Run comprehensive diagnostics
python manage.py revolution --status
python manage.py revolution --validate
python manage.py revolution --validate-zones
python manage.py revolution --test-schemas
```

### Log Files

```bash
# Check Django logs
tail -f logs/django.log

# Check system logs
journalctl -u your-service -f
```

### Community Support

- 🐛 [GitHub Issues](https://github.com/markolofsen/django-revolution/issues)
- 💬 [GitHub Discussions](https://github.com/markolofsen/django-revolution/discussions)
- 📧 [Email Support](mailto:developers@unrealos.com)

### Debug Information

When reporting issues, include:

```bash
# System information
python --version
django-admin --version
node --version
npm --version

# Django Revolution version
python -c "import django_revolution; print(django_revolution.__version__)"

# Configuration
python manage.py revolution --status

# Error logs
python manage.py revolution --debug 2>&1
```

---

[← Back to Usage](usage.html) | [Next: API Reference →](api-reference.html)
