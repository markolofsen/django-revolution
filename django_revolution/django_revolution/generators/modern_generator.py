"""
Modern Python Client Generator using openapi-python-client

Clean, simple, and powerful generator with excellent enum support.
"""

from pathlib import Path
from typing import Dict, Optional, Any
import traceback
import datetime
import sys
import subprocess

from ..config import GenerationResult
from ..utils import Logger, run_command, ensure_directories


class ModernPythonGenerator:
    """
    Modern Python client generator using openapi-python-client.
    
    Features:
    - Excellent enum support (generates proper Enum classes, not Optional[str])
    - Pydantic v2 compatibility
    - Modern Python 3.8+ features
    - Type-safe code generation
    - Async/sync support
    - Clean, idiomatic code
    """
    
    def __init__(self, config=None, logger: Optional[Logger] = None):
        """Initialize the generator."""
        self.config = config
        self.logger = logger or Logger("modern_python_generator")
        
        if config:
            self.output_dir = Path(config.generators.python.output_directory)
        else:
            self.output_dir = Path.cwd() / "openapi" / "clients" / "python"
    
    def is_available(self) -> bool:
        """Check if openapi-python-client is available."""
        try:
            # Try direct command
            result = subprocess.run(
                ["openapi-python-client", "--version"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0:
                self.logger.info("openapi-python-client available via direct command")
                return True
            
            # Try with pipx
            result = subprocess.run(
                ["pipx", "run", "openapi-python-client", "--version"], 
                capture_output=True, 
                text=True, 
                timeout=15
            )
            if result.returncode == 0:
                self.logger.info("openapi-python-client available via pipx")
                return True
            
            # Try as Python module
            result = subprocess.run(
                ["python", "-m", "openapi_python_client", "--version"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0:
                self.logger.info("openapi-python-client available as Python module")
                return True
            
            self.logger.warning("openapi-python-client not found")
            return False
            
        except Exception as e:
            self.logger.error(f"Error checking openapi-python-client availability: {e}")
            return False
    
    def generate_client(self, zone_name: str, schema_path: Path) -> GenerationResult:
        """Generate Python client using openapi-python-client."""
        self.logger.info(f"🚀 Generating modern Python client for zone: {zone_name}")
        
        # Validate schema file
        if not schema_path.exists():
            error_msg = f"Schema file not found: {schema_path}"
            self.logger.error(error_msg)
            return GenerationResult(
                success=False,
                zone_name=zone_name,
                output_path=Path(),
                files_generated=0,
                error_message=error_msg,
            )
        
        # Setup output directory
        zone_output_dir = self.output_dir / zone_name
        ensure_directories(zone_output_dir)
        
        try:
            # Get the appropriate command
            cmd = self._get_command()
            
            # Build command for openapi-python-client with optimal settings
            full_cmd = cmd + [
                "generate",
                "--path", str(schema_path),
                "--output-path", str(zone_output_dir),
                "--overwrite",  # Always overwrite for clean generation
            ]
            
            # Create config file for better enum generation
            config_file = self._create_config_file(zone_name, zone_output_dir)
            if config_file:
                full_cmd.extend(["--config", str(config_file)])
            
            self.logger.info(f"Running: {' '.join(full_cmd)}")
            
            # Execute the command
            result = subprocess.run(
                full_cmd,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=Path.cwd()
            )
            
            if result.returncode == 0:
                # Check if files were generated
                generated_files = list(zone_output_dir.rglob("*.py"))
                
                if generated_files:
                    files_count = len(generated_files)
                    
                    # Enhance the generated client
                    self._enhance_client(zone_name, zone_output_dir)
                    
                    # Format generated Python files
                    self._format_python_files(zone_output_dir)
                    
                    self.logger.success(
                        f"✅ Modern Python client generated for {zone_name}: {files_count} files"
                    )
                    
                    return GenerationResult(
                        success=True,
                        zone_name=zone_name,
                        output_path=zone_output_dir,
                        files_generated=files_count,
                        error_message="",
                    )
                else:
                    error_msg = f"No Python files generated in: {zone_output_dir}"
                    self.logger.error(error_msg)
                    return GenerationResult(
                        success=False,
                        zone_name=zone_name,
                        output_path=zone_output_dir,
                        files_generated=0,
                        error_message=error_msg,
                    )
            else:
                error_msg = f"openapi-python-client failed: {result.stderr}"
                self.logger.error(error_msg)
                self._save_error_log(zone_name, zone_output_dir, full_cmd, error_msg, result.stderr)
                
                return GenerationResult(
                    success=False,
                    zone_name=zone_name,
                    output_path=zone_output_dir,
                    files_generated=0,
                    error_message=error_msg,
                )
        
        except Exception as e:
            error_msg = f"Exception during generation: {str(e)}"
            self.logger.error(error_msg)
            
            # Get full traceback
            tb = traceback.format_exc()
            self.logger.error(f"Full traceback:\n{tb}")
            
            self._save_error_log(zone_name, zone_output_dir, [], error_msg, tb)
            
            return GenerationResult(
                success=False,
                zone_name=zone_name,
                output_path=zone_output_dir,
                files_generated=0,
                error_message=error_msg,
            )
    
    def generate_all(self, schemas: Dict[str, Path]) -> Dict[str, GenerationResult]:
        """Generate Python clients for all provided schemas."""
        if not schemas:
            self.logger.warning("No schemas provided for Python generation")
            return {}
        
        self.logger.info(f"🚀 Generating modern Python clients for {len(schemas)} zones")
        
        results = {}
        for zone_name, schema_path in schemas.items():
            result = self.generate_client(zone_name, schema_path)
            results[zone_name] = result
        
        successful = sum(1 for r in results.values() if r.success)
        self.logger.info(
            f"✅ Modern Python generation completed: {successful}/{len(results)} successful"
        )
        
        return results
    
    def _get_command(self) -> list:
        """Get the appropriate command to run openapi-python-client."""
        # Try different ways to run the command
        commands_to_try = [
            ["openapi-python-client"],
            ["pipx", "run", "openapi-python-client"],
            ["python", "-m", "openapi_python_client"],
        ]
        
        for cmd in commands_to_try:
            try:
                result = subprocess.run(
                    cmd + ["--version"], 
                    capture_output=True, 
                    timeout=10
                )
                if result.returncode == 0:
                    return cmd
            except Exception:
                continue
        
        # Fallback to direct command
        return ["openapi-python-client"]
    
    def _enhance_client(self, zone_name: str, output_dir: Path):
        """Enhance the generated client with additional features."""
        try:
            # Create a simple __init__.py for easier imports
            init_file = output_dir / "__init__.py"
            if not init_file.exists():
                init_content = f'''"""
{zone_name.title()} API Client

Generated by Django Revolution using openapi-python-client.
Modern Python client with excellent enum support.
"""

# Import main client classes
try:
    from .client import Client, AuthenticatedClient
    from .api import *
    from .models import *
    
    __all__ = ["Client", "AuthenticatedClient"]
except ImportError:
    # Fallback for different client structures
    pass

__version__ = "1.0.0"
__generator__ = "openapi-python-client"
'''
                with open(init_file, "w", encoding="utf-8") as f:
                    f.write(init_content)
                
                self.logger.debug(f"Created enhanced __init__.py for {zone_name}")
        
        except Exception as e:
            self.logger.debug(f"Could not enhance client for {zone_name}: {e}")
    
    def _format_python_files(self, directory: Path) -> bool:
        """Format Python files using ruff (included with openapi-python-client)."""
        try:
            # Try to format with ruff (comes with openapi-python-client)
            result = subprocess.run(
                ["ruff", "format", str(directory)],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                self.logger.info("🎨 Python files formatted with ruff")
                return True
            else:
                # Try with black as fallback
                result = subprocess.run(
                    ["black", "--line-length", "88", str(directory)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    self.logger.info("🎨 Python files formatted with black")
                    return True
                else:
                    self.logger.debug("No formatter available, skipping formatting")
                    return True
                
        except Exception as e:
            self.logger.debug(f"Could not format Python files: {e}")
            return True  # Don't fail generation due to formatting issues
    
    def _create_config_file(self, zone_name: str, output_dir: Path) -> Optional[Path]:
        """Create configuration file for openapi-python-client."""
        try:
            config_content = {
                # Critical settings for proper enum generation
                "use_string_enums": False,  # Generate proper Enum classes, not strings
                "generate_aliases": True,   # Better field names
                "use_pydantic_v2": True,    # Modern Pydantic
                
                # Additional settings for stability
                "project_name_override": f"django_revolution_{zone_name}",
                "package_name_override": f"django_revolution_{zone_name}",
                "client_class_name": f"{zone_name.title()}Client",
                
                # Code quality settings
                "post_hooks": [
                    "ruff format .",
                    "ruff check . --fix",
                ],
                
                # HTTP settings
                "http_timeout": 30,
                "follow_redirects": True,
            }
            
            config_file = output_dir / "openapi_config.yaml"
            
            import yaml
            with open(config_file, "w", encoding="utf-8") as f:
                yaml.dump(config_content, f, default_flow_style=False)
            
            self.logger.debug(f"Created config file: {config_file}")
            return config_file
            
        except Exception as e:
            self.logger.warning(f"Could not create config file: {e}")
            return None

    def _save_error_log(self, zone_name: str, output_dir: Path, cmd: list, error_msg: str, output: str):
        """Save detailed error log to file."""
        log_file = output_dir / f"error_{zone_name}.log"
        try:
            with open(log_file, "w", encoding="utf-8") as f:
                f.write(f"=== Modern Python Client Generation Error ===\n")
                f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
                f.write(f"Zone: {zone_name}\n")
                f.write(f"Output: {output_dir}\n")
                f.write(f"Command: {' '.join(cmd)}\n")
                f.write(f"\n=== Error Details ===\n")
                f.write(f"Error: {error_msg}\n")
                f.write(f"\n=== Full Output ===\n")
                f.write(f"{output}\n")
                f.write(f"\n=== Environment Info ===\n")
                f.write(f"Python Version: {sys.version}\n")
                f.write(f"Working Directory: {Path.cwd()}\n")
        except Exception as log_exc:
            self.logger.error(f"Failed to write detailed error log: {log_exc}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get generator status."""
        return {
            "generator": "openapi-python-client",
            "available": self.is_available(),
            "output_directory": str(self.output_dir),
            "features": [
                "Excellent enum support",
                "Pydantic v2 compatibility", 
                "Modern Python 3.8+",
                "Type-safe code generation",
                "Async/sync support"
            ]
        }
