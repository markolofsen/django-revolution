---
layout: default
title: CLI Reference
---

# CLI Reference

**Command-line interface for Django Revolution.**

## 🎯 Overview

Django Revolution provides multiple CLI interfaces:

- **Django Management Command** - `python manage.py revolution`
- **Standalone CLI** - `django-revolution`
- **Development Scripts** - `scripts/dev_cli.py`
- **Individual Tools** - Version management, publishing, requirements generation

## 🚀 Django Management Commands

### Generate Clients

```bash
# Interactive generation (default)
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

### Status and Information

```bash
# Check status
python manage.py revolution --status

# List available zones
python manage.py revolution --list-zones

# Show help
python manage.py revolution --help
```

### Validation and Testing

```bash
# Validate each zone with detailed logging
python manage.py revolution --validate-zones

# Show URL patterns for each zone
python manage.py revolution --show-urls

# Test schema generation for each zone
python manage.py revolution --test-schemas

# Validate environment
python manage.py revolution --validate
```

### Dependencies

```bash
# Install dependencies
python manage.py revolution --install-deps

# Check dependencies
python manage.py revolution --check-deps
```

### Archive Management

```bash
# Generate with archive
python manage.py revolution --archive

# List archives
python manage.py revolution --list-archives

# Download specific archive
python manage.py revolution --download-archive 2024-01-15_10-30-00

# Clean archives
python manage.py revolution --clean-archives
```

### Monorepo

```bash
# Sync to monorepo
python manage.py revolution --monorepo

# Skip monorepo sync
python manage.py revolution --no-monorepo
```

## 🎨 Standalone CLI

### Interactive Mode

```bash
# Rich interactive interface
django-revolution

# Or run directly
python -m django_revolution.cli
```

The standalone CLI provides:

- 🎯 Zone selection with checkboxes
- 🔧 Client type selection (TypeScript/Python)
- 📦 Archive creation options
- 📊 Real-time progress tracking
- ✅ Generation summary with results table

### Command Line Mode

```bash
# Direct generation
django-revolution --zones public,admin --typescript --python

# Status check
django-revolution --status

# Zone validation
django-revolution --validate-zones
```

## 🛠️ Development Scripts

### Interactive Development CLI

```bash
# Main development interface
python scripts/dev_cli.py

# Or install and use as package command
pip install -e .
dev-cli
```

Provides interactive access to:
- 📦 Version Management
- 🚀 Package Publishing
- 🧪 Test Generation
- 📋 Requirements Generation
- 🔧 Package Building

### Individual Scripts

```bash
# Version management
python scripts/version_manager.py get
python scripts/version_manager.py bump --bump-type patch
python scripts/version_manager.py validate

# Generate requirements files
python scripts/generate_requirements.py

# Interactive publishing
python scripts/publisher.py

# Test generation
./scripts/test_generation.sh
```

### Package Commands (after installation)

```bash
# Version management
version-manager get
version-manager bump --bump-type minor
version-manager validate

# Publishing
publisher

# Requirements generation
generate-requirements
```

## 📋 Command Options

### Django Management Command

| Option               | Description              | Example                                  |
| -------------------- | ------------------------ | ---------------------------------------- |
| `--zones`            | Generate specific zones  | `--zones public admin`                   |
| `--typescript`       | Generate TypeScript only | `--typescript`                           |
| `--python`           | Generate Python only     | `--python`                               |
| `--archive`          | Create archive           | `--archive`                              |
| `--no-archive`       | Skip archive creation    | `--no-archive`                           |
| `--monorepo`         | Sync to monorepo         | `--monorepo`                             |
| `--no-monorepo`      | Skip monorepo sync       | `--no-monorepo`                          |
| `--clean`            | Clean output directory   | `--clean`                                |
| `--status`           | Show status              | `--status`                               |
| `--list-zones`       | List zones               | `--list-zones`                           |
| `--validate-zones`   | Validate zones           | `--validate-zones`                       |
| `--show-urls`        | Show zone URLs           | `--show-urls`                            |
| `--test-schemas`     | Test schema generation   | `--test-schemas`                         |
| `--validate`         | Validate environment     | `--validate`                             |
| `--install-deps`     | Install dependencies     | `--install-deps`                         |
| `--check-deps`       | Check dependencies       | `--check-deps`                           |
| `--list-archives`    | List archives            | `--list-archives`                        |
| `--download-archive` | Download archive         | `--download-archive 2024-01-15_10-30-00` |
| `--clean-archives`   | Clean archives           | `--clean-archives`                       |
| `--help`             | Show help                | `--help`                                 |

### Version Manager

| Option               | Description              | Example                                  |
| -------------------- | ------------------------ | ---------------------------------------- |
| `get`                | Get current version      | `version-manager get`                    |
| `bump`               | Bump version             | `version-manager bump --bump-type patch` |
| `validate`           | Validate versions        | `version-manager validate`               |
| `requirements`       | Regenerate requirements  | `version-manager requirements`           |
| `--bump-type`        | Version bump type        | `--bump-type [major\|minor\|patch]`      |

## 🔧 Examples

### Development Workflow

```bash
# 1. Start development CLI
python scripts/dev_cli.py

# 2. Check status
python manage.py revolution --status

# 3. Generate clients for development
python manage.py revolution --zones public

# 4. Test generation
python manage.py revolution --test-schemas

# 5. Bump version
python scripts/version_manager.py bump --bump-type patch

# 6. Generate requirements
python scripts/generate_requirements.py

# 7. Build and publish
python scripts/publisher.py
```

### CI/CD Pipeline

```bash
# Install dependencies
python manage.py revolution --install-deps

# Validate environment
python manage.py revolution --validate

# Generate clients
python manage.py revolution --archive

# Sync to monorepo
python manage.py revolution --monorepo
```

### Troubleshooting

```bash
# Check what's wrong
python manage.py revolution --status

# Validate zones
python manage.py revolution --validate-zones

# Test schema generation
python manage.py revolution --test-schemas

# Clean and regenerate
python manage.py revolution --clean
python manage.py revolution

# Check dependencies
python manage.py revolution --check-deps
```

## 🎯 Rich Output Examples

**Zone Validation:**
```
╭───────────────────────────────────────────── 🧪 Validation ──────────────────────────────────────────────╮
│ Detailed Zone Validation                                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
==================================================

🔍 Validating zone: public
------------------------------
  ✅ Zone configuration: Public API
  Apps (1):
    ✅ apps.public_api
  ✅ URL patterns: 1 patterns
  ✅ Schema patterns: 2 patterns
  ✅ Zone 'public' is valid

📊 Validation Summary:
  Valid zones: 2
  Invalid zones: 0
🎉 All zones are valid!
```

**Generation Results:**
```
╭───────────────────────────────────────────── 📊 Results ──────────────────────────────────────────────────╮
│ Generation completed successfully!                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
==================================================

📁 Generated Files:
  ✅ openapi/schemas/public.yaml (2.1 KB)
  ✅ openapi/schemas/admin.yaml (1.8 KB)
  ✅ clients/typescript/index.ts (15.2 KB)
  ✅ clients/python/client.py (12.7 KB)
  ✅ openapi/archive/2024-01-15_10-30-00.zip (28.3 KB)

📊 Summary:
  Zones processed: 2
  TypeScript files: 3
  Python files: 2
  Archive created: Yes
```

---

[← Back to Usage](usage.html) | [Next: API Reference →](api-reference.html)
