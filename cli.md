---
layout: default
title: CLI Reference
---

# CLI Reference

**Command-line interface for Django Revolution.**

## Basic Commands

### Generate Clients

```bash
# Generate all clients
python manage.py revolution

# Generate specific zones
python manage.py revolution --zones public admin

# TypeScript only
python manage.py revolution --typescript

# Python only
python manage.py revolution --python
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

## Command Options

| Option               | Description              | Example                                  |
| -------------------- | ------------------------ | ---------------------------------------- |
| `--zones`            | Generate specific zones  | `--zones public admin`                   |
| `--typescript`       | Generate TypeScript only | `--typescript`                           |
| `--python`           | Generate Python only     | `--python`                               |
| `--archive`          | Create archive           | `--archive`                              |
| `--monorepo`         | Sync to monorepo         | `--monorepo`                             |
| `--no-monorepo`      | Skip monorepo sync       | `--no-monorepo`                          |
| `--clean`            | Clean output directory   | `--clean`                                |
| `--status`           | Show status              | `--status`                               |
| `--list-zones`       | List zones               | `--list-zones`                           |
| `--install-deps`     | Install dependencies     | `--install-deps`                         |
| `--check-deps`       | Check dependencies       | `--check-deps`                           |
| `--list-archives`    | List archives            | `--list-archives`                        |
| `--download-archive` | Download archive         | `--download-archive 2024-01-15_10-30-00` |
| `--clean-archives`   | Clean archives           | `--clean-archives`                       |
| `--help`             | Show help                | `--help`                                 |

## Examples

### Development Workflow

```bash
# 1. Check status
python manage.py revolution --status

# 2. Generate clients for development
python manage.py revolution --zones public

# 3. Generate all clients for production
python manage.py revolution --archive --monorepo
```

### CI/CD Pipeline

```bash
# Install dependencies
python manage.py revolution --install-deps

# Generate clients
python manage.py revolution --archive

# Sync to monorepo
python manage.py revolution --monorepo
```

### Troubleshooting

```bash
# Check what's wrong
python manage.py revolution --status

# Clean and regenerate
python manage.py revolution --clean
python manage.py revolution

# Check dependencies
python manage.py revolution --check-deps
```

---

[← Back to Usage](usage.html) | [Next: API Reference →](api-reference.html)
