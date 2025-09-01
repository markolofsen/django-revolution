"""
Tests for Django Revolution configuration.
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
    GeneratorsSettings,
    GenerationResult,
    GenerationSummary
)


class TestDjangoRevolutionSettings:
    """Test DjangoRevolutionSettings configuration."""

    def test_default_settings(self):
        """Test default settings values."""
        config = DjangoRevolutionSettings()
        
        assert config.api_prefix == "apix"
        assert config.debug is False
        assert config.auto_install_deps is True
        assert config.version == "1.0.32"
        assert config.enable_multithreading is True
        assert config.max_workers == 20
        assert isinstance(config.output, OutputSettings)
        assert isinstance(config.generators, GeneratorsSettings)
        assert config.zones == {}

    def test_custom_settings(self):
        """Test custom settings values."""
        config = DjangoRevolutionSettings(
            api_prefix="custom",
            debug=True,
            version="2.0.0",
            enable_multithreading=False,
            max_workers=10
        )
        
        assert config.api_prefix == "custom"
        assert config.debug is True
        assert config.version == "2.0.0"
        assert config.enable_multithreading is False
        assert config.max_workers == 10

    def test_zones_configuration(self):
        """Test zones configuration."""
        zones = {
            "public": {
                "apps": ["django.contrib.auth"],
                "title": "Public API",
                "description": "Public API endpoints",
                "public": True,
                "version": "v1"
            }
        }
        
        config = DjangoRevolutionSettings(zones=zones)
        assert len(config.zones) == 1
        assert "public" in config.zones

    def test_to_dict(self):
        """Test to_dict method."""
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

    def test_get_zones(self):
        """Test get_zones method."""
        zones = {
            "public": {
                "apps": ["django.contrib.auth"],
                "title": "Public API",
                "version": "v1"
            }
        }
        
        config = DjangoRevolutionSettings(zones=zones)
        zone_models = config.get_zones()
        
        assert len(zone_models) == 1
        assert "public" in zone_models
        assert isinstance(zone_models["public"], ZoneModel)
        assert zone_models["public"].name == "public"
        assert zone_models["public"].apps == ["django.contrib.auth"]

    def test_get_zone(self):
        """Test get_zone method."""
        zones = {
            "public": {
                "apps": ["django.contrib.auth"],
                "title": "Public API",
                "version": "v1"
            }
        }
        
        config = DjangoRevolutionSettings(zones=zones)
        
        zone = config.get_zone("public")
        assert zone is not None
        assert isinstance(zone, ZoneModel)
        assert zone.name == "public"
        
        zone = config.get_zone("nonexistent")
        assert zone is None


class TestZoneModel:
    """Test ZoneModel configuration."""

    def test_zone_model_creation(self):
        """Test ZoneModel creation."""
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
        """Test ZoneModel default values."""
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

    def test_zone_model_validation(self):
        """Test ZoneModel validation."""
        # Test empty apps list
        with pytest.raises(ValidationError):
            ZoneModel(name="test", apps=[])
        
        # Test empty name
        with pytest.raises(ValidationError):
            ZoneModel(name="", apps=["django.contrib.auth"])
        
        # Test whitespace name
        with pytest.raises(ValidationError):
            ZoneModel(name="   ", apps=["django.contrib.auth"])


class TestOutputSettings:
    """Test OutputSettings configuration."""

    def test_output_settings_defaults(self):
        """Test OutputSettings default values."""
        settings = OutputSettings()
        
        assert "openapi" in settings.base_directory
        assert settings.schemas_directory == "schemas"
        assert settings.clients_directory == "clients"
        assert settings.temp_directory == "temp"

    def test_output_settings_custom(self):
        """Test OutputSettings custom values."""
        settings = OutputSettings(
            base_directory="/custom/path",
            schemas_directory="custom_schemas",
            clients_directory="custom_clients"
        )
        
        assert settings.base_directory == "/custom/path"
        assert settings.schemas_directory == "custom_schemas"
        assert settings.clients_directory == "custom_clients"


class TestGeneratorSettings:
    """Test generator settings."""

    def test_typescript_generator_settings(self):
        """Test TypeScriptGeneratorSettings."""
        settings = TypeScriptGeneratorSettings(
            enabled=True,
            output_directory="/custom/ts",
            output_format="prettier",
            generate_tests=True
        )
        
        assert settings.enabled is True
        assert settings.output_directory == "/custom/ts"
        assert settings.output_format == "prettier"
        assert settings.generate_tests is True

    def test_python_generator_settings(self):
        """Test PythonGeneratorSettings."""
        settings = PythonGeneratorSettings(
            enabled=True,
            output_directory="/custom/py",
            project_name_template="custom_{zone}",
            package_name_template="custom_{zone}",
            overwrite=True
        )
        
        assert settings.enabled is True
        assert settings.output_directory == "/custom/py"
        assert settings.project_name_template == "custom_{zone}"
        assert settings.package_name_template == "custom_{zone}"
        assert settings.overwrite is True


class TestGenerationResult:
    """Test GenerationResult model."""

    def test_generation_result_creation(self):
        """Test GenerationResult creation."""
        result = GenerationResult(
            success=True,
            zone_name="test",
            output_path=Path("/test/path"),
            files_generated=5,
            error_message=""
        )
        
        assert result.success is True
        assert result.zone_name == "test"
        assert result.output_path == Path("/test/path")
        assert result.files_generated == 5
        assert result.error_message == ""

    def test_generation_result_failure(self):
        """Test GenerationResult for failed generation."""
        result = GenerationResult(
            success=False,
            zone_name="test",
            output_path=Path("/test/path"),
            files_generated=0,
            error_message="Test error"
        )
        
        assert result.success is False
        assert result.files_generated == 0
        assert result.error_message == "Test error"


class TestGenerationSummary:
    """Test GenerationSummary model."""

    def test_generation_summary_creation(self):
        """Test GenerationSummary creation."""
        summary = GenerationSummary(
            total_zones=2,
            successful_typescript=1,
            successful_python=1,
            failed_typescript=0,
            failed_python=0,
            total_files_generated=10,
            duration_seconds=5.5
        )
        
        assert summary.total_zones == 2
        assert summary.successful_typescript == 1
        assert summary.successful_python == 1
        assert summary.failed_typescript == 0
        assert summary.failed_python == 0
        assert summary.total_files_generated == 10
        assert summary.duration_seconds == 5.5


class TestMultithreadingSettings:
    """Test multithreading configuration."""

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

    def test_multithreading_in_to_dict(self):
        """Test that multithreading settings are included in to_dict()."""
        config = DjangoRevolutionSettings(
            enable_multithreading=True,
            max_workers=10
        )
        
        config_dict = config.to_dict()
        
        assert "enable_multithreading" in config_dict
        assert "max_workers" in config_dict
        assert config_dict["enable_multithreading"] is True
        assert config_dict["max_workers"] == 10 