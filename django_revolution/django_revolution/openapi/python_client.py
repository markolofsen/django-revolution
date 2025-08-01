"""
Python Client Generator for Django Revolution

Generates Python clients using openapi-python-generator.
"""

from pathlib import Path
from typing import Dict, Optional, Any
import traceback
import datetime
import sys

from ..config import DjangoRevolutionSettings, GenerationResult
from ..utils import Logger, run_command, check_dependency, ensure_directories


class PythonClientGenerator:
    """Python client generator using openapi-python-generator."""

    def __init__(
        self, config: DjangoRevolutionSettings, logger: Optional[Logger] = None
    ):
        """
        Initialize Python generator.

        Args:
            config: Django Revolution settings
            logger: Optional logger instance
        """
        self.config = config
        self.logger = logger or Logger("python_client_generator")
        self.output_dir = Path(config.generators.python.output_directory)

    def is_openapi_generator_available(self) -> bool:
        """
        Check if openapi-python-generator is available.

        Returns:
            bool: True if available
        """
        # Try direct import first
        try:
            import openapi_python_generator
            self.logger.info(f"openapi-python-generator imported successfully")
            return True
        except ImportError:
            self.logger.warning(f"openapi-python-generator import failed")
        
        # Try different ways to run the command
        from ..utils import run_command
        
        # Try 1: Direct command
        success, output = run_command("openapi-python-generator --version")
        if success:
            self.logger.info(f"openapi-python-generator available via direct command")
            return True
            
        # Try 2: Poetry run
        success, output = run_command("poetry run openapi-python-generator --version")
        if success:
            self.logger.info(f"openapi-python-generator available via poetry run")
            return True
            
        # Try 3: Python module
        success, output = run_command("python -m openapi_python_generator --version")
        if success:
            self.logger.info(f"openapi-python-generator available via python module")
            return True
            
        self.logger.warning(f"openapi-python-generator not found in any environment")
        return False

    def generate_client(self, zone_name: str, schema_path: Path) -> GenerationResult:
        """
        Generate Python client for a single zone.

        Args:
            zone_name: Name of the zone
            schema_path: Path to OpenAPI schema file

        Returns:
            GenerationResult with operation details
        """
        self.logger.info(f"Generating Python client for zone: {zone_name}")

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

        # Use openapi-python-generator
        if self.is_openapi_generator_available():
            return self._generate_with_openapi_generator(
                zone_name, schema_path, zone_output_dir
            )

        error_msg = (
            "No Python client generators available. Install 'openapi-python-generator'"
        )
        self.logger.error(error_msg)
        return GenerationResult(
            success=False,
            zone_name=zone_name,
            output_path=zone_output_dir,
            files_generated=0,
            error_message=error_msg,
        )

    def _get_openapi_generator_command(self) -> list:
        """
        Get the appropriate command to run openapi-python-generator.
        
        Returns:
            List of command parts
        """
        from ..utils import run_command
        
        # Try 1: Direct command
        success, _ = run_command("openapi-python-generator --version")
        if success:
            return ["openapi-python-generator"]
            
        # Try 2: Poetry run
        success, _ = run_command("poetry run openapi-python-generator --version")
        if success:
            return ["poetry", "run", "openapi-python-generator"]
            
        # Try 3: Python module
        success, _ = run_command("python -m openapi_python_generator --version")
        if success:
            return ["python", "-m", "openapi_python_generator"]
            
        # Fallback to poetry run (most common case)
        return ["poetry", "run", "openapi-python-generator"]

    def _generate_with_openapi_generator(
        self, zone_name: str, schema_path: Path, zone_output_dir: Path
    ) -> GenerationResult:
        """
        Generate Python client using openapi-python-generator.

        Args:
            zone_name: Name of the zone
            schema_path: Path to OpenAPI schema file
            zone_output_dir: Output directory for the zone

        Returns:
            GenerationResult with operation details
        """
        self.logger.info(f"Using openapi-python-generator for {zone_name}")

        try:
            # Generate project and package names
            project_name = self.config.generators.python.project_name_template.format(
                zone=zone_name
            )

            # Get the appropriate command
            base_cmd = self._get_openapi_generator_command()
            
            # Build command for openapi-python-generator
            cmd = base_cmd + [
                str(schema_path),
                str(zone_output_dir),
            ]

            success, output = run_command(" ".join(cmd), timeout=120)

            if success:
                # Check if files were generated
                # openapi-python-generator creates a directory structure
                models_dir = zone_output_dir / "models"
                services_dir = zone_output_dir / "services"
                
                if models_dir.exists() or services_dir.exists():
                    # Count generated files
                    files_generated = self._count_generated_files(zone_output_dir)

                    # Enhance the generated client
                    self._enhance_openapi_client(
                        zone_name, zone_output_dir
                    )

                    self.logger.success(
                        f"Python client generated with openapi-python-generator for {zone_name}: {files_generated} files"
                    )

                    return GenerationResult(
                        success=True,
                        zone_name=zone_name,
                        output_path=zone_output_dir,
                        files_generated=files_generated,
                        error_message="",
                    )
                else:
                    error_msg = f"openapi-python-generator did not create expected files in: {zone_output_dir}"
                    self.logger.error(error_msg)
                    return GenerationResult(
                        success=False,
                        zone_name=zone_name,
                        output_path=zone_output_dir,
                        files_generated=0,
                        error_message=error_msg,
                    )
            else:
                error_msg = f"openapi-python-generator failed: {output}"
                self.logger.error(error_msg)

                # Save detailed error to log file
                log_file = zone_output_dir / f"error_{zone_name}.log"
                try:
                    with open(log_file, "w", encoding="utf-8") as f:
                        f.write(
                            f"=== Python Client Generation Error (openapi-python-generator) ===\n"
                        )
                        f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
                        f.write(f"Zone: {zone_name}\n")
                        f.write(f"Schema: {schema_path}\n")
                        f.write(f"Output: {zone_output_dir}\n")
                        f.write(f"Command: {' '.join(cmd)}\n")
                        f.write(f"\n=== Error Details ===\n")
                        f.write(f"Error: {error_msg}\n")
                        f.write(f"Command Exit Code: Non-zero (command failed)\n")
                        f.write(f"\n=== Full Command Output ===\n")
                        f.write(f"{output}\n")
                        f.write(f"\n=== Environment Info ===\n")
                        f.write(f"Python Version: {sys.version}\n")
                        f.write(f"Working Directory: {Path.cwd()}\n")
                except Exception as log_exc:
                    self.logger.error(f"Failed to write detailed error log: {log_exc}")

                return GenerationResult(
                    success=False,
                    zone_name=zone_name,
                    output_path=zone_output_dir,
                    files_generated=0,
                    error_message=error_msg,
                )

        except Exception as e:
            error_msg = f"openapi-python-generator exception: {str(e)}"
            self.logger.error(error_msg)

            # Get full traceback with all details
            tb = traceback.format_exc()
            self.logger.error(f"Full traceback:\n{tb}")

            # Save detailed error log to file
            log_file = zone_output_dir / f"error_{zone_name}.log"
            try:
                with open(log_file, "w", encoding="utf-8") as f:
                    f.write(
                        f"=== Python Client Generation Error (openapi-python-generator) ===\n"
                    )
                    f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
                    f.write(f"Zone: {zone_name}\n")
                    f.write(f"Schema: {schema_path}\n")
                    f.write(f"Output: {zone_output_dir}\n")
                    f.write(f"Command: {' '.join(cmd)}\n")
                    f.write(f"\n=== Error Details ===\n")
                    f.write(f"Error: {error_msg}\n")
                    f.write(f"Exception Type: {type(e).__name__}\n")
                    f.write(f"\n=== Full Traceback ===\n")
                    f.write(f"{tb}\n")
                    f.write(f"\n=== Environment Info ===\n")
                    f.write(f"Python Version: {sys.version}\n")
                    f.write(f"Working Directory: {Path.cwd()}\n")
            except Exception as log_exc:
                self.logger.error(f"Failed to write detailed error log: {log_exc}")

            return GenerationResult(
                success=False,
                zone_name=zone_name,
                output_path=zone_output_dir,
                files_generated=0,
                error_message=error_msg,
            )

    def generate_all(self, schemas: Dict[str, Path]) -> Dict[str, GenerationResult]:
        """
        Generate Python clients for all provided schemas.

        Args:
            schemas: Dictionary mapping zone names to schema paths

        Returns:
            Dictionary mapping zone names to generation results
        """
        if not schemas:
            self.logger.warning("No schemas provided for Python generation")
            return {}

        self.logger.info(f"Generating Python clients for {len(schemas)} zones")

        results = {}

        for zone_name, schema_path in schemas.items():
            result = self.generate_client(zone_name, schema_path)
            results[zone_name] = result

        successful = sum(1 for r in results.values() if r.success)
        self.logger.info(
            f"Python generation completed: {successful}/{len(results)} successful"
        )

        return results

    def _count_generated_files(self, directory: Path) -> int:
        """
        Count the number of generated files in a directory.

        Args:
            directory: Directory to count files in

        Returns:
            Number of files generated
        """
        if not directory.exists():
            return 0

        count = 0
        for file_path in directory.rglob("*"):
            if file_path.is_file() and not file_path.name.startswith("."):
                # Count all files except error logs
                if not file_path.name.startswith("error_"):
                    count += 1

        return count

    def _enhance_openapi_client(
        self, zone_name: str, output_dir: Path
    ):
        """
        Enhance the generated openapi-python-generator client with additional features.

        Args:
            zone_name: Name of the zone
            output_dir: Output directory for the zone
        """
        # No additional enhancement needed - openapi-python-generator provides everything
        self.logger.debug(f"Using openapi-python-generator output for {zone_name}")



    def _generate_requirements(self, zone_name: str, output_dir: Path):
        """Generate a requirements.txt file for the datamodel client."""
        try:
            requirements_content = """pydantic>=2.0.0
requests>=2.25.0
typing-extensions>=4.0.0
"""

            requirements_file = output_dir / "requirements.txt"
            with open(requirements_file, "w", encoding="utf-8") as f:
                f.write(requirements_content)

        except Exception as e:
            self.logger.debug(f"Could not generate requirements.txt: {e}")

    def clean_output(self) -> bool:
        """
        Clean Python output directory.

        Returns:
            bool: True if cleaning successful
        """
        try:
            if self.output_dir.exists():
                import shutil

                shutil.rmtree(self.output_dir)

            ensure_directories(self.output_dir)
            self.logger.success("Python output directory cleaned")
            return True

        except Exception as e:
            self.logger.error(f"Failed to clean Python output directory: {e}")
            return False

    def get_status(self) -> Dict[str, Any]:
        """
        Get Python generator status.

        Returns:
            Status information dictionary
        """
        return {
            "available": self.is_openapi_generator_available(),
            "output_directory": str(self.output_dir),
            "enabled": self.config.generators.python.enabled,
            "project_name_template": self.config.generators.python.project_name_template,
            "package_name_template": self.config.generators.python.package_name_template,
            "overwrite": self.config.generators.python.overwrite,
            "fail_on_warning": self.config.generators.python.fail_on_warning,
            "custom_templates": self.config.generators.python.custom_templates,
        }
