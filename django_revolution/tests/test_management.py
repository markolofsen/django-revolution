"""
Tests for Django Revolution management commands.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from io import StringIO

from django_revolution.management.commands.revolution import Command
from django_revolution.config import DjangoRevolutionSettings


class TestRevolutionCommand:
    """Test Django Revolution management command."""

    def setup_method(self):
        """Set up test command."""
        from django_revolution.management.commands.revolution import Command
        self.command = Command()

    def setUp(self):
        """Set up test configuration."""
        self.test_zones = {
            "public": {
                "apps": ["django.contrib.auth", "django.contrib.contenttypes"],
                "title": "Public API",
                "description": "Public API endpoints",
                "public": True,
                "version": "v1"
            },
            "admin": {
                "apps": ["django.contrib.admin"],
                "title": "Admin API",
                "description": "Admin API endpoints",
                "public": False,
                "auth_required": True,
                "version": "v1"
            }
        }
        
        self.config = DjangoRevolutionSettings(
            zones=self.test_zones,
            enable_multithreading=True,
            max_workers=4
        )
        self.command = Command()

    def test_add_arguments(self):
        """Test that all arguments are properly added."""
        from django.core.management.base import CommandParser
        
        parser = CommandParser()
        self.command.add_arguments(parser)
        
        # Check that all expected arguments are present
        expected_args = [
            '--generate', '--zones', '--typescript', '--python',
            '--no-typescript', '--no-python', '--no-archive',
            '--clean', '--no-multithreading', '--max-workers', '--status',
            '--list-zones', '--validate-zones', '--show-urls', '--test-schemas',
            '--interactive', '--verbose', '--output-dir'
        ]
        
        for arg in expected_args:
            # Check if argument exists in parser
            found = False
            for action in parser._actions:
                if arg in action.option_strings:
                    found = True
                    break
            assert found, f"Argument {arg} not found in parser"

    def test_handle_generate(self):
        """Test handle method with generate flag."""
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'zones': ['public'],
                'typescript': True,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_multithreading': False,
                'max_workers': None,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            self.command.handle(**options)
            
            # Verify that cli.main was called with correct arguments
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--generate' in call_args
            assert '--zones' in call_args
            assert 'public' in call_args
            assert '--typescript' in call_args
            assert '--no-python' in call_args

    def test_handle_status(self):
        """Test handle method with status flag."""
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': False,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_multithreading': False,
                'max_workers': None,
                'status': True,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            self.command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--status' in call_args

    def test_handle_multithreading_options(self):
        """Test handle method with multithreading options."""
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_monorepo': False,
                'no_multithreading': True,
                'max_workers': 10,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            self.command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--no-multithreading' in call_args
            assert '--max-workers' in call_args
            assert '10' in call_args

    def test_handle_clean_option(self):
        """Test handle method with clean option."""
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': True,
                'no_archive': False,
                'no_multithreading': False,
                'max_workers': None,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            self.command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--clean' in call_args

    def test_handle_output_dir(self):
        """Test handle method with output directory."""
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_multithreading': False,
                'max_workers': None,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': '/custom/output'
            }
            
            self.command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--output-dir' in call_args
            assert '/custom/output' in call_args

    def test_handle_interactive(self):
        """Test handle method with interactive flag."""
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': False,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_multithreading': False,
                'max_workers': None,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': True,
                'verbose': False,
                'output_dir': None
            }
            
            self.command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--interactive' in call_args


class TestMultithreadingManagement:
    """Test multithreading options in management command."""

    def test_no_multithreading_option(self):
        """Test --no-multithreading option."""
        command = Command()
        
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'no_multithreading': True,
                'max_workers': None,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_monorepo': False,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--no-multithreading' in call_args

    def test_max_workers_option(self):
        """Test --max-workers option."""
        command = Command()
        
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'no_multithreading': False,
                'max_workers': 15,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_monorepo': False,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--max-workers' in call_args
            assert '15' in call_args

    def test_multithreading_options_combination(self):
        """Test combination of multithreading options."""
        command = Command()
        
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': True,
                'no_multithreading': True,
                'max_workers': 8,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_monorepo': False,
                'status': False,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--no-multithreading' in call_args
            assert '--max-workers' in call_args
            assert '8' in call_args

    def test_status_with_multithreading_info(self):
        """Test that status includes multithreading information."""
        command = Command()
        
        with patch('django_revolution.management.commands.revolution.cli.main') as mock_cli_main:
            options = {
                'generate': False,
                'no_multithreading': False,
                'max_workers': None,
                'zones': None,
                'typescript': False,
                'python': False,
                'clean': False,
                'no_archive': False,
                'no_monorepo': False,
                'status': True,
                'list_zones': False,
                'validate_zones': False,
                'show_urls': False,
                'test_schemas': False,
                'interactive': False,
                'verbose': False,
                'output_dir': None
            }
            
            command.handle(**options)
            
            mock_cli_main.assert_called_once()
            call_args = mock_cli_main.call_args[0][0]
            assert '--status' in call_args 