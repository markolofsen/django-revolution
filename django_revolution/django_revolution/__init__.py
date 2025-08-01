"""
Django Revolution - Universal Zone-Based API Client Generator

A powerful library for generating OpenAPI schemas and client libraries 
organized by API zones using Django REST Framework and drf-spectacular.

Key Features:
- Zone-based API architecture
- Automatic OpenAPI schema generation with multithreading support
- TypeScript and Python client generation  
- Archive management and monorepo integration
- Django management commands
- Comprehensive validation and error handling

Usage:
    from django_revolution import ZoneManager, OpenAPIGenerator
    from django_revolution.config import get_settings
    
    # Initialize with configuration
    config = get_settings()
    generator = OpenAPIGenerator(config)
    
    # Generate all clients
    summary = generator.generate_all()
    
    # Or generate specific zones
    summary = generator.generate_all(zones=['public', 'admin'])
"""

from .config import DjangoRevolutionSettings, ZoneModel, get_settings, MonorepoConfig
from .zones import ZoneManager, ZoneDetector
from .openapi import OpenAPIGenerator, MultiMonorepoSync
from .utils import Logger, ErrorHandler
from .urls_integration import add_revolution_urls, get_revolution_urlpatterns, get_revolution_urls_info

__version__ = "1.0.26"
__author__ = "Unrealos Team"
__description__ = "Universal Zone-Based API Client Generator for Django"

__all__ = [
    # Core components
    'OpenAPIGenerator',
    'ZoneManager', 
    'ZoneDetector',
    'MultiMonorepoSync',
    'MonorepoConfig',

    # URL Integration
    'add_revolution_urls',
    'get_revolution_urlpatterns',
    'get_revolution_urls_info',
    
    # Utilities
    'Logger',
    'ErrorHandler',
    
    # Metadata
    '__version__',
    '__author__',
    '__description__',
]


def create_generator(config=None):
    """
    Convenience function to create an OpenAPIGenerator instance.
    
    Args:
        config: Optional DjangoRevolutionSettings instance
        
    Returns:
        OpenAPIGenerator: Configured generator instance
    """
    if config is None:
        config = get_settings()
    return OpenAPIGenerator(config)


def quick_generate(zones=None, typescript=True, python=True, archive=True):
    """
    Quick generation function for common use cases.
    
    Args:
        zones: List of zone names to generate (None for all)
        typescript: Whether to generate TypeScript clients
        python: Whether to generate Python clients  
        archive: Whether to archive generated clients
        
    Returns:
        GenerationSummary: Summary of generation results
    """
    generator = create_generator()
    
    # Set generator options - enable both by default
    generator.config.generators.typescript.enabled = typescript
    generator.config.generators.python.enabled = python
        
    return generator.generate_all(zones=zones, archive=archive) 