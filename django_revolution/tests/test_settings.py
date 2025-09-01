"""
Tests for Django Revolution settings management.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, Mock
from pydantic import ValidationError

from django_revolution.config import DjangoRevolutionSettings, get_settings, get_config


class TestSettingsManagement:
    """Test settings management functionality."""

    def test_get_settings_default(self):
        """Test getting default settings."""
        settings = get_settings()
        
        assert isinstance(settings, DjangoRevolutionSettings)
        assert settings.api_prefix == "apix"
        assert settings.debug is False
        assert settings.auto_install_deps is True
        assert settings.version == "1.0.32"
        assert settings.enable_multithreading is False  # Default is False
        assert settings.max_workers == 10  # Default is 10

    def test_get_settings_singleton(self):
        """Test that get_settings returns the same instance."""
        settings1 = get_settings()
        settings2 = get_settings()
        
        assert settings1 is settings2

    def test_get_config(self):
        """Test getting configuration as dictionary."""
        config = get_config()
        
        assert isinstance(config, dict)
        assert "api_prefix" in config
        assert "debug" in config
        assert "version" in config
        assert "enable_multithreading" in config
        assert "max_workers" in config
        assert "output" in config
        assert "generators" in config
        assert "zones" in config

    def test_settings_with_custom_values(self):
        """Test settings with custom values."""
        settings = DjangoRevolutionSettings(
            api_prefix="custom",
            debug=True,
            version="2.0.0",
            enable_multithreading=False,
            max_workers=5
        )
        
        assert settings.api_prefix == "custom"
        assert settings.debug is True
        assert settings.version == "2.0.0"
        assert settings.enable_multithreading is False
        assert settings.max_workers == 5

    def test_settings_validation(self):
        """Test settings validation."""
        # Test valid settings
        settings = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        assert len(settings.zones) == 1
        assert "public" in settings.zones

    def test_settings_invalid_zones(self):
        """Test settings with invalid zones."""
        # Test duplicate apps
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

    def test_settings_zone_validation(self):
        """Test zone validation in settings."""
        # Test empty apps list
        with pytest.raises(ValidationError):
            DjangoRevolutionSettings(
                zones={
                    "zone1": {
                        "apps": [],
                        "title": "Zone 1",
                        "version": "v1"
                    }
                }
            )

    def test_settings_output_configuration(self):
        """Test output configuration in settings."""
        settings = DjangoRevolutionSettings(
            output={
                "base_directory": "/custom/path",
                "schemas_directory": "custom_schemas",
                "clients_directory": "custom_clients"
            }
        )
        
        assert settings.output.base_directory == "/custom/path"
        assert settings.output.schemas_directory == "custom_schemas"
        assert settings.output.clients_directory == "custom_clients"

    def test_settings_generators_configuration(self):
        """Test generators configuration in settings."""
        settings = DjangoRevolutionSettings(
            generators={
                "typescript": {
                    "enabled": False,
                    "output_directory": "/custom/ts"
                },
                "python": {
                    "enabled": True,
                    "output_directory": "/custom/py"
                }
            }
        )
        
        assert settings.generators.typescript.enabled is False
        assert settings.generators.typescript.output_directory == "/custom/ts"
        assert settings.generators.python.enabled is True
        assert settings.generators.python.output_directory == "/custom/py"



    def test_settings_to_dict(self):
        """Test settings to_dict method."""
        settings = DjangoRevolutionSettings(
            api_prefix="test",
            debug=True,
            version="1.0.0",
            enable_multithreading=True,
            max_workers=10
        )
        
        config_dict = settings.to_dict()
        
        assert config_dict["api_prefix"] == "test"
        assert config_dict["debug"] is True
        assert config_dict["version"] == "1.0.0"
        assert config_dict["enable_multithreading"] is True
        assert config_dict["max_workers"] == 10
        assert "output" in config_dict
        assert "generators" in config_dict
        assert "zones" in config_dict

    def test_settings_get_zones(self):
        """Test get_zones method."""
        settings = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        zones = settings.get_zones()
        
        assert len(zones) == 1
        assert "public" in zones
        assert zones["public"].name == "public"
        assert zones["public"].apps == ["django.contrib.auth"]

    def test_settings_get_zone(self):
        """Test get_zone method."""
        settings = DjangoRevolutionSettings(
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        zone = settings.get_zone("public")
        assert zone is not None
        assert zone.name == "public"
        
        zone = settings.get_zone("nonexistent")
        assert zone is None


class TestMultithreadingSettings:
    """Test multithreading settings specifically."""

    def test_multithreading_defaults(self):
        """Test default multithreading settings."""
        settings = DjangoRevolutionSettings()
        
        assert settings.enable_multithreading is True
        assert settings.max_workers == 20

    def test_multithreading_custom_values(self):
        """Test custom multithreading values."""
        settings = DjangoRevolutionSettings(
            enable_multithreading=False,
            max_workers=5
        )
        
        assert settings.enable_multithreading is False
        assert settings.max_workers == 5

    def test_multithreading_in_to_dict(self):
        """Test that multithreading settings are included in to_dict()."""
        settings = DjangoRevolutionSettings(
            enable_multithreading=True,
            max_workers=15
        )
        
        config_dict = settings.to_dict()
        
        assert "enable_multithreading" in config_dict
        assert "max_workers" in config_dict
        assert config_dict["enable_multithreading"] is True
        assert config_dict["max_workers"] == 15

    def test_multithreading_validation(self):
        """Test multithreading settings validation."""
        # Test valid max_workers values
        settings1 = DjangoRevolutionSettings(max_workers=1)
        assert settings1.max_workers == 1
        
        settings2 = DjangoRevolutionSettings(max_workers=50)
        assert settings2.max_workers == 50

    def test_multithreading_with_zones(self):
        """Test multithreading settings with zones."""
        settings = DjangoRevolutionSettings(
            enable_multithreading=True,
            max_workers=4,
            zones={
                "public": {
                    "apps": ["django.contrib.auth"],
                    "title": "Public API",
                    "version": "v1"
                }
            }
        )
        
        assert settings.enable_multithreading is True
        assert settings.max_workers == 4 