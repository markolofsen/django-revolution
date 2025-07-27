---
layout: default
title: Usage
---

# 🚀 Usage Guide - LLM-Optimized

## 📖 Overview

Comprehensive usage guide for Django Revolution with performance optimization, multithreading, and advanced configuration patterns.

**Key Features:**
- **Multithreaded generation** - Parallel processing for performance
- **Zone-specific generation** - Generate specific zones only
- **Performance optimization** - Configurable worker threads and memory management
- **CI/CD integration** - Automated workflows and artifact management

---

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

### ⚡ Multithreaded Generation

```bash
# Use default multithreading (20 workers)
python manage.py revolution --generate

# Custom number of worker threads
python manage.py revolution --generate --max-workers 16

# Disable multithreading for debugging
python manage.py revolution --generate --no-multithreading

# Performance optimization for large projects
python manage.py revolution --generate --max-workers 32 --clean
```

### 🔍 Validation & Testing

```bash
# Validate all zones
python manage.py revolution --validate-zones

# Test schema generation
python manage.py revolution --test-schemas

# Show URL patterns
python manage.py revolution --show-urls

# Check status
python manage.py revolution --status
```

---

## 🎯 Advanced Usage

### Performance Optimization

#### Multithreading Configuration

```python
# settings.py - Optimize for your system
DJANGO_REVOLUTION = {
    'enable_multithreading': True,
    'max_workers': 20,  # Adjust based on your CPU cores
    # ... other settings
}
```

#### Worker Thread Guidelines

| System Type | Recommended Workers | Use Case |
|-------------|-------------------|----------|
| **Development** | 4-8 | Local development |
| **CI/CD** | 8-16 | Automated builds |
| **Production** | 16-32 | High-performance servers |
| **Large Projects** | 32-64 | Enterprise applications |

#### Memory Management

```bash
# Clean before generation
python manage.py revolution --clean --generate

# Monitor memory usage
python manage.py revolution --generate --max-workers 8

# Batch processing for large projects
for zone in public admin internal; do
    python manage.py revolution --zones $zone --clean
done
```

### Zone-Specific Generation

```bash
# Generate only public zone
python manage.py revolution --zones public

# Generate multiple specific zones
python manage.py revolution --zones public admin internal

# Generate with custom output
python manage.py revolution --zones public --output-dir /custom/path
```

### Client Type Selection

```bash
# TypeScript only
python manage.py revolution --typescript

# Python only
python manage.py revolution --python

# Both (default)
python manage.py revolution --typescript --python
```

---

## 🔧 Configuration Examples

### Basic Zone Configuration

```python
# settings.py
from django_revolution.app_config import ZoneConfig, get_revolution_config

zones = {
    'public': ZoneConfig(
        apps=['accounts', 'billing'],
        title='Public API',
        description='Public API endpoints',
        public=True,
        auth_required=False,
        version='v1'
    ),
    'admin': ZoneConfig(
        apps=['admin_panel', 'analytics'],
        title='Admin API',
        description='Administrative endpoints',
        public=False,
        auth_required=True,
        version='v1'
    )
}

DJANGO_REVOLUTION = get_revolution_config(
    project_root=BASE_DIR,
    zones=zones,
    debug=DEBUG
)
```

### Multithreading Configuration

```python
# settings.py - Performance optimized
DJANGO_REVOLUTION = {
    'enable_multithreading': True,
    'max_workers': 20,  # Adjust based on your system
    'zones': zones,
    'output': {
        'base_directory': BASE_DIR / 'openapi',
        'schemas_directory': 'schemas',
        'clients_directory': 'clients',
    },
    'generators': {
        'typescript': {
            'enabled': True,
            'output_format': 'prettier',
        },
        'python': {
            'enabled': True,
            'overwrite': True,
        }
    }
}
```

### Environment-Specific Configuration

```python
# settings/development.py
DJANGO_REVOLUTION = {
    'enable_multithreading': True,
    'max_workers': 8,  # Lower for development
    'debug': True,
    # ... zones configuration
}

# settings/production.py
DJANGO_REVOLUTION = {
    'enable_multithreading': True,
    'max_workers': 32,  # Higher for production
    'debug': False,
    # ... zones configuration
}
```

---

## 📊 Performance Monitoring

### Generation Time Tracking

```bash
# Time the generation process
time python manage.py revolution --generate

# Compare sequential vs multithreaded
time python manage.py revolution --generate --no-multithreading
time python manage.py revolution --generate --max-workers 16
```

### Memory Usage Monitoring

```bash
# Monitor memory usage during generation
python manage.py revolution --generate --max-workers 8 2>&1 | tee generation.log

# Check for memory leaks
python manage.py revolution --generate --clean
```

### Worker Thread Optimization

```bash
# Test different worker counts
for workers in 4 8 16 32; do
    echo "Testing with $workers workers:"
    time python manage.py revolution --generate --max-workers $workers --clean
done
```

---

## 🧪 Testing & Validation

### Zone Validation

```bash
# Validate all zones
python manage.py revolution --validate-zones

# Expected output:
# ✅ Zone 'public' is valid
# ✅ Zone 'admin' is valid
# 🎉 All zones are valid!
```

### Schema Testing

```bash
# Test schema generation
python manage.py revolution --test-schemas

# Expected output:
# ✅ Schema generated: public.yaml (14KB)
# ✅ Schema generated: admin.yaml (33KB)
# 🎉 All schema tests passed!
```

### URL Pattern Inspection

```bash
# Show URL patterns
python manage.py revolution --show-urls

# Expected output:
# PUBLIC ZONE:
#   • public_api/
#   • schema/ -> public-schema
#   • schema/swagger/ -> public-swagger
```

---

## 🔄 CI/CD Integration

### GitHub Actions Example

```yaml
# .github/workflows/generate-clients.yml
name: Generate API Clients

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          pip install poetry
          poetry install
          
      - name: Generate API clients
        run: |
          poetry run python manage.py revolution --generate --max-workers 8 --clean
          
      - name: Upload generated clients
        uses: actions/upload-artifact@v3
        with:
          name: api-clients
          path: openapi/clients/
```

### GitLab CI Example

```yaml
# .gitlab-ci.yml
generate_clients:
  stage: build
  image: python:3.10
  script:
    - pip install poetry
    - poetry install
    - poetry run python manage.py revolution --generate --max-workers 8 --clean
  artifacts:
    paths:
      - openapi/clients/
    expire_in: 1 week
```

---

## 🚨 Troubleshooting

### Common Performance Issues

**Slow Generation:**
```bash
# Enable multithreading
python manage.py revolution --generate --max-workers 16

# Clean before generation
python manage.py revolution --clean --generate

# Check system resources
htop  # or top
```

**Memory Issues:**
```bash
# Reduce worker count
python manage.py revolution --generate --max-workers 4

# Clean between generations
python manage.py revolution --clean

# Monitor memory usage
python manage.py revolution --generate --debug
```

**Django Setup Issues:**
```bash
# Check Django settings
python manage.py check

# Validate environment
python manage.py revolution --validate

# Debug mode
python manage.py revolution --debug --verbosity 3
```

### Debug Mode

```bash
# Enable debug logging
python manage.py revolution --debug

# Maximum verbosity
python manage.py revolution --verbosity 3

# Show full stack traces
python manage.py revolution --traceback
```

---

## 📈 Best Practices

### Performance Optimization

1. **Use multithreading** - Enable for multiple zones
2. **Optimize worker count** - Match your CPU cores
3. **Clean regularly** - Remove old generated files
4. **Monitor resources** - Watch memory and CPU usage
5. **Batch processing** - Generate zones separately if needed

### Configuration Management

1. **Environment-specific configs** - Different settings per environment
2. **Version control** - Track configuration changes
3. **Validation** - Always validate zones before generation
4. **Testing** - Test schema generation regularly
5. **Documentation** - Document zone configurations

### CI/CD Integration

1. **Automated generation** - Generate on every deployment
2. **Artifact management** - Store generated clients as artifacts
3. **Performance monitoring** - Track generation times
4. **Error handling** - Proper error reporting and recovery
5. **Caching** - Cache dependencies for faster builds

---

## 🧠 Key Notes

- **Multithreading performance** - 2-3x speedup for multiple zones
- **Memory optimization** - Configurable worker threads and cleanup
- **CI/CD ready** - Automated workflows with artifact management
- **Environment flexibility** - Different configs for dev/prod
- **Monitoring tools** - Built-in performance tracking and validation
- **Best practices** - Comprehensive guidelines for optimal usage

---

[← Back to Installation](installation.html) | [Next: CLI Reference →](cli.html)
