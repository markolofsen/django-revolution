---
layout: default
title: Troubleshooting
---

# Troubleshooting

**Common issues and solutions for Django Revolution.**

## Installation Issues

### ImportError: No module named 'django_revolution'

**Problem**: Django Revolution is not installed or not in Python path.

**Solution**:

```bash
# Install Django Revolution
pip install django-revolution

# Verify installation
python -c "import django_revolution; print('✅ Installed')"
```

### ModuleNotFoundError: No module named 'django_filters'

**Problem**: Missing dependencies.

**Solution**:

```bash
# Install missing dependencies
pip install django-filter djangorestframework-simplejwt

# Or let Django Revolution install them
python manage.py revolution --install-deps
```

## Configuration Issues

### Zone Configuration Error

**Problem**: Invalid zone configuration in settings.

**Solution**:

```python
# settings.py - Correct format
DJANGO_REVOLUTION = {
    'zones': {
        'public': {
            'apps': ['accounts', 'billing'],  # List of apps
            'title': 'Public API',
            'description': 'Public endpoints',
            'public': True,
            'auth_required': False,
            'version': 'v1',
            'path_prefix': 'public'
        }
    }
}
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

## Generation Issues

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
```

### OpenAPI Schema Generation Fails

**Problem**: Schema generation errors.

**Solution**:

```bash
# Check Django setup
python manage.py check

# Check DRF configuration
python manage.py spectacular --help

# Generate schema manually
python manage.py spectacular --file openapi/schema.yaml

# Then run revolution
python manage.py revolution
```

### TypeScript Generation Fails

**Problem**: Node.js or npm issues.

**Solution**:

```bash
# Check Node.js installation
node --version
npm --version

# Install Node.js if missing
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS
brew install node

# Windows
choco install nodejs

# Fix npm permissions (Linux/macOS)
sudo chown -R $(whoami) ~/.npm
```

### Python Client Generation Fails

**Problem**: Python client generation errors.

**Solution**:

```bash
# Install Python dependencies
pip install openapi-python-client

# Check Python version (3.8+ required)
python --version

# Clean and retry
python manage.py revolution --clean
python manage.py revolution
```

## Monorepo Issues

### Monorepo Sync Fails

**Problem**: Cannot sync to monorepo.

**Solution**:

```bash
# Check monorepo configuration
python manage.py revolution --status

# Verify project_root path
# settings.py
DJANGO_REVOLUTION = {
    'monorepo': {
        'enabled': True,
        'project_root': BASE_DIR.parent,  # Correct path
        'packages_dir': 'packages',
    }
}

# Skip monorepo sync if needed
python manage.py revolution --no-monorepo
```

### Package.json Not Found

**Problem**: Missing package.json in monorepo.

**Solution**:

```bash
# Create package.json if missing
echo '{"name": "my-monorepo"}' > package.json

# Or disable monorepo sync
python manage.py revolution --no-monorepo
```

## Performance Issues

### Slow Generation

**Problem**: Client generation takes too long.

**Solution**:

```bash
# Generate specific zones only
python manage.py revolution --zones public

# Skip archive creation
python manage.py revolution  # No --archive flag

# Skip monorepo sync
python manage.py revolution --no-monorepo
```

### Memory Issues

**Problem**: Out of memory during generation.

**Solution**:

```bash
# Generate zones separately
python manage.py revolution --zones public
python manage.py revolution --zones private

# Increase Python memory limit
python -X maxsize=2G manage.py revolution
```

## Archive Issues

### Archive Creation Fails

**Problem**: Cannot create archives.

**Solution**:

```bash
# Check disk space
df -h

# Check write permissions
ls -la openapi/

# Clean old archives
python manage.py revolution --clean-archives

# Try without archive
python manage.py revolution  # No --archive flag
```

### Archive Download Fails

**Problem**: Cannot download archives.

**Solution**:

```bash
# List available archives
python manage.py revolution --list-archives

# Check archive format
ls -la openapi/archive/

# Download specific archive
python manage.py revolution --download-archive 2024-01-15_10-30-00
```

## Debugging

### Enable Verbose Logging

```bash
# Set debug environment variable
export DJANGO_REVOLUTION_DEBUG=1

# Run with verbose output
python manage.py revolution --status
```

### Check Status

```bash
# Comprehensive status check
python manage.py revolution --status

# Check dependencies
python manage.py revolution --check-deps

# List zones
python manage.py revolution --list-zones
```

### Common Error Messages

| Error                                 | Cause                     | Solution                         |
| ------------------------------------- | ------------------------- | -------------------------------- |
| `No module named 'django_revolution'` | Not installed             | `pip install django-revolution`  |
| `Command not found: revolution`       | App not in INSTALLED_APPS | Add to INSTALLED_APPS            |
| `Node.js not found`                   | Node.js not installed     | Install Node.js                  |
| `Permission denied`                   | npm permissions           | `sudo chown -R $(whoami) ~/.npm` |
| `Schema generation failed`            | DRF configuration         | Check DRF settings               |
| `Monorepo sync failed`                | Invalid project_root      | Check path in settings           |

## Getting Help

### Before Asking for Help

1. **Check status**: `python manage.py revolution --status`
2. **Check dependencies**: `python manage.py revolution --check-deps`
3. **Enable debug**: `export DJANGO_REVOLUTION_DEBUG=1`
4. **Check logs**: Look for error messages in output

### Resources

- 📖 [Documentation](https://django-revolution.readthedocs.io/)
- 🐛 [GitHub Issues](https://github.com/markolofsen/django-revolution/issues)
- 💬 [Discussions](https://github.com/markolofsen/django-revolution/discussions)
- 📧 [Email Support](mailto:developers@unrealos.com)

---

[← Back to Architecture](architecture.html) | [Back to Home](index.html)
