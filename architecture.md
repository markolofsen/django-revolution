---
layout: default
title: Architecture
---

# Architecture

**Understanding Django Revolution's zone-based architecture.**

## Overview

Django Revolution introduces a **zone-based architecture** that organizes your Django API into logical, isolated sections. Each zone represents a different context or access level for your API endpoints.

## Zone-Based Architecture

### What are Zones?

Zones are logical groupings of API endpoints that share common characteristics:

- **Access level** (public, private, internal, admin)
- **Authentication requirements** (none, JWT, session)
- **Rate limiting** (different limits per zone)
- **Documentation** (separate OpenAPI schemas)
- **Client generation** (zone-specific clients)

### Zone Types

#### Public Zone

- **Purpose**: External-facing API endpoints
- **Authentication**: Optional (JWT or none)
- **Rate Limiting**: Strict
- **Examples**: User registration, product catalog, public data

#### Private Zone

- **Purpose**: Authenticated user endpoints
- **Authentication**: Required (JWT)
- **Rate Limiting**: Moderate
- **Examples**: User profile, orders, personal data

#### Internal Zone

- **Purpose**: Internal service communication
- **Authentication**: Service-to-service
- **Rate Limiting**: High
- **Examples**: Microservice APIs, internal tools

#### Admin Zone

- **Purpose**: Administrative operations
- **Authentication**: Admin users only
- **Rate Limiting**: Low
- **Examples**: User management, analytics, system config

## Architecture Components

### 1. Zone Configuration

```python
# settings.py
DJANGO_REVOLUTION = {
    'zones': {
        'public': {
            'apps': ['accounts', 'products'],
            'title': 'Public API',
            'description': 'Public endpoints',
            'public': True,
            'auth_required': False,
            'version': 'v1',
            'path_prefix': 'public'
        },
        'private': {
            'apps': ['orders', 'profile'],
            'title': 'Private API',
            'description': 'Authenticated endpoints',
            'public': False,
            'auth_required': True,
            'version': 'v1',
            'path_prefix': 'private'
        }
    }
}
```

### 2. URL Structure

Django Revolution automatically creates a structured URL hierarchy:

```
/api/
├── public/
│   ├── schema/          # Swagger UI
│   ├── schema.yaml      # OpenAPI spec
│   └── v1/              # API endpoints
├── private/
│   ├── schema/
│   ├── schema.yaml
│   └── v1/
└── admin/
    ├── schema/
    ├── schema.yaml
    └── v1/
```

### 3. Client Generation

Each zone generates its own client:

```
clients/
├── typescript/
│   ├── public/
│   │   ├── index.ts
│   │   └── types.ts
│   ├── private/
│   │   ├── index.ts
│   │   └── types.ts
│   └── index.ts         # Main client
└── python/
    ├── public/
    │   ├── __init__.py
    │   └── client.py
    ├── private/
    │   ├── __init__.py
    │   └── client.py
    └── __init__.py      # Main client
```

## Data Flow

### 1. Request Flow

```
Client Request
    ↓
Zone Router (Django Revolution)
    ↓
Zone-specific Middleware
    ↓
Authentication Check
    ↓
Rate Limiting
    ↓
Django View
    ↓
Response
```

### 2. Client Generation Flow

```
Django Models & Views
    ↓
Zone Detection
    ↓
OpenAPI Schema Generation
    ↓
Client Template Rendering
    ↓
Generated Clients
    ↓
Monorepo Sync (optional)
```

## Benefits

### 1. Security

- **Isolation**: Each zone has its own security context
- **Granular Control**: Different auth requirements per zone
- **Rate Limiting**: Zone-specific limits

### 2. Maintainability

- **Clear Structure**: Logical organization of endpoints
- **Independent Evolution**: Zones can evolve separately
- **Documentation**: Zone-specific documentation

### 3. Client Experience

- **Type Safety**: Zone-specific TypeScript types
- **IntelliSense**: Better IDE support
- **Error Handling**: Zone-specific error handling

### 4. Development

- **Parallel Development**: Teams can work on different zones
- **Testing**: Zone-specific test suites
- **Deployment**: Independent zone deployment

## Best Practices

### 1. Zone Design

- **Single Responsibility**: Each zone should have a clear purpose
- **Minimal Coupling**: Zones should be as independent as possible
- **Consistent Naming**: Use clear, descriptive zone names

### 2. Security

- **Principle of Least Privilege**: Grant minimum required access
- **Regular Audits**: Review zone permissions regularly
- **Monitoring**: Monitor zone usage and access patterns

### 3. Performance

- **Caching**: Zone-specific caching strategies
- **Rate Limiting**: Appropriate limits for each zone
- **Optimization**: Zone-specific optimizations

### 4. Documentation

- **Clear Descriptions**: Document each zone's purpose
- **Examples**: Provide usage examples for each zone
- **Migration Guides**: Document zone changes

## Migration Strategy

### From Monolithic API

1. **Identify Zones**: Analyze existing endpoints
2. **Create Zones**: Define zone boundaries
3. **Move Endpoints**: Gradually move endpoints to zones
4. **Update Clients**: Update client code to use zones
5. **Test**: Comprehensive testing of each zone

### From Microservices

1. **Consolidate**: Group related services into zones
2. **Standardize**: Use consistent patterns across zones
3. **Optimize**: Remove redundant code and configurations
4. **Document**: Create comprehensive documentation

---

[← Back to API Reference](api-reference.html) | [Next: Troubleshooting →](troubleshooting.html)
