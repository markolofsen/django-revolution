"""
Tests for basic Django Revolution functionality.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, Mock
from pydantic import ValidationError

from django_revolution.config import (
    DjangoRevolutionSettings, 
    ZoneModel, 
    OutputSettings,
    TypeScriptGeneratorSettings,
    PythonGeneratorSettings,
    GeneratorsSettings
)
from django_revolution.openapi.generator import OpenAPIGenerator


class TestBasicFunctionality:
    """Test basic Django Revolution functionality."""

    def test_import_django_revolution(self):
        """Test that django_revolution can be imported."""
        import django_revolution
        assert django_revolution.__version__ == "1.0.32"

    def test_create_basic_config(self):
        """Test creating a basic configuration."""
        config = DjangoRevolutionSettings()
        
        assert config.api_prefix == "apix"
        assert config.debug is False
        assert config.auto_install_deps is True
        assert config.version == "1.0.32"
        assert config.enable_multithreading is True
        assert config.max_workers == 20

    def test_create_zone_model(self):
        """Test creating a zone model."""
        zone = ZoneModel(
            name="test",
            apps=["django.contrib.auth"],
            title="Test Zone",
            description="Test zone description",
            public=True,
            auth_required=False,
            version="v1"
        )
        
        assert zone.name == "test"
        assert zone.apps == ["django.contrib.auth"]
        assert zone.title == "Test Zone"
        assert zone.description == "Test zone description"
        assert zone.public is True
        assert zone.auth_required is False
        assert zone.version == "1.0.32"

    def test_zone_model_defaults(self):
        """Test zone model default values."""
        zone = ZoneModel(
            name="test",
            apps=["django.contrib.auth"]
        )
        
        assert zone.name == "test"
        assert zone.apps == ["django.contrib.auth"]
        assert zone.title is None  # Title is not auto-generated anymore
        assert zone.public is True
        assert zone.auth_required is False
        assert zone.version == "1.0.32"
        assert zone.path_prefix == "test"  # Auto-generated from name

    def test_config_with_zones(self):
        """Test configuration with zones."""
        config = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        assert len(config.zones) == 1
        assert "public" in config.zones

    def test_get_zones_from_config(self):
        """Test getting zones from configuration."""
        config = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        zones = config.get_zones()
        
        assert len(zones) == 1
        assert "public" in zones
        assert isinstance(zones["public"], ZoneModel)
        assert zones["public"].name == "public"
        assert zones["public"].apps == ["django.contrib.auth"]

    def test_get_single_zone(self):
        """Test getting a single zone."""
        config = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        zone = config.get_zone("public")
        assert zone is not None
        assert isinstance(zone, ZoneModel)
        assert zone.name == "public"
        
        zone = config.get_zone("nonexistent")
        assert zone is None

    def test_config_to_dict(self):
        """Test converting configuration to dictionary."""
        config = DjangoRevolutionSettings(
            api_prefix="test",
            debug=True,
            version="1.0.0",
            enable_multithreading=True,
            max_workers=5
        )
        
        config_dict = config.to_dict()
        
        assert config_dict["api_prefix"] == "test"
        assert config_dict["debug"] is True
        assert config_dict["version"] == "1.0.0"
        assert config_dict["enable_multithreading"] is True
        assert config_dict["max_workers"] == 5
        assert "output" in config_dict
        assert "generators" in config_dict
        assert "zones" in config_dict


class TestMultithreadingBasics:
    """Test basic multithreading functionality."""

    def test_multithreading_defaults(self):
        """Test default multithreading settings."""
        config = DjangoRevolutionSettings()
        
        assert config.enable_multithreading is True
        assert config.max_workers == 20

    def test_multithreading_custom(self):
        """Test custom multithreading settings."""
        config = DjangoRevolutionSettings(
            enable_multithreading=False,
            max_workers=5
        )
        
        assert config.enable_multithreading is False
        assert config.max_workers == 5

    def test_multithreading_in_dict(self):
        """Test that multithreading settings are in to_dict()."""
        config = DjangoRevolutionSettings(
            enable_multithreading=True,
            max_workers=10
        )
        
        config_dict = config.to_dict()
        
        assert "enable_multithreading" in config_dict
        assert "max_workers" in config_dict
        assert config_dict["enable_multithreading"] is True
        assert config_dict["max_workers"] == 10


class TestGeneratorBasics:
    """Test basic generator functionality."""

    def test_generator_creation(self):
        """Test creating a generator."""
        config = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        with patch('django_revolution.openapi.generator.get_django_manage_py') as mock_manage_py:
            mock_manage_py.return_value = Path("/tmp/manage.py")
            
            generator = OpenAPIGenerator(config)
            
            assert generator.config == config
            assert generator.zone_manager is not None
            assert len(generator.zone_manager.zones) == 1

    def test_generator_status(self):
        """Test generator status."""
        config = DjangoRevolutionSettings()
        
        with patch('django_revolution.openapi.generator.get_django_manage_py') as mock_manage_py:
            mock_manage_py.return_value = Path("/tmp/manage.py")
            
            generator = OpenAPIGenerator(config)
            status = generator.get_status()
            
            assert "multithreading" in status
            assert status["multithreading"]["enabled"] is True
            assert status["multithreading"]["max_workers"] == 20
            assert status["multithreading"]["threading_available"] is True


class TestValidation:
    """Test validation functionality."""

    def test_zone_validation_empty_apps(self):
        """Test zone validation with empty apps list."""
        with pytest.raises(ValidationError):
            ZoneModel(name="test", apps=[])

    def test_zone_validation_empty_name(self):
        """Test zone validation with empty name."""
        with pytest.raises(ValidationError):
            ZoneModel(name="", apps=["django.contrib.auth"])

    def test_zone_validation_whitespace_name(self):
        """Test zone validation with whitespace name."""
        with pytest.raises(ValidationError):
            ZoneModel(name="   ", apps=["django.contrib.auth"])

    def test_config_validation_duplicate_apps(self):
        """Test configuration validation with duplicate apps."""
        with pytest.raises(ValueError, match="Duplicate apps across zones"):
            DjangoRevolutionSettings(
                zones={
                    "zone1": {
                        "apps": ["django.contrib.auth"],
                        "title": "Zone 1",
                        "version": "v1"
                    },
                    "zone2": {
                        "apps": ["django.contrib.auth"],  # Duplicate app
                        "title": "Zone 2",
                        "version": "v1"
                    }
                }
            )

    def test_config_validation_duplicate_prefixes(self):
        """Test configuration validation with duplicate prefixes."""
        with pytest.raises(ValueError, match="Duplicate path prefix"):
            DjangoRevolutionSettings(
                zones={
                    "zone1": {
                        "apps": ["django.contrib.auth"],
                        "title": "Zone 1",
                        "path_prefix": "same",
                        "version": "v1"
                    },
                    "zone2": {
                        "apps": ["django.contrib.contenttypes"],
                        "title": "Zone 2",
                        "path_prefix": "same",  # Duplicate prefix
                        "version": "v1"
                    }
                }
            ) 