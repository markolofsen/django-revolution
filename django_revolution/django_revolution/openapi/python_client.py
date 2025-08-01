"""
Python Client Generator for Django Revolution

Generates Python clients using datamodel-code-generator.
"""

from pathlib import Path
from typing import Dict, Optional, Any
import traceback
import datetime
import sys

from ..config import DjangoRevolutionSettings, GenerationResult
from ..utils import Logger, run_command, check_dependency, ensure_directories


class PythonClientGenerator:
    """Python client generator using datamodel-code-generator."""

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

    def is_datamodel_available(self) -> bool:
        """
        Check if datamodel-code-generator is available.

        Returns:
            bool: True if available
        """
        return check_dependency(["datamodel-codegen", "--version"])

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

        # Use datamodel-code-generator
        if self.is_datamodel_available():
            return self._generate_with_datamodel(
                zone_name, schema_path, zone_output_dir
            )

        error_msg = (
            "No Python client generators available. Install 'datamodel-code-generator'"
        )
        self.logger.error(error_msg)
        return GenerationResult(
            success=False,
            zone_name=zone_name,
            output_path=zone_output_dir,
            files_generated=0,
            error_message=error_msg,
        )

    def _generate_with_datamodel(
        self, zone_name: str, schema_path: Path, zone_output_dir: Path
    ) -> GenerationResult:
        """
        Generate Python client using datamodel-code-generator.

        Args:
            zone_name: Name of the zone
            schema_path: Path to OpenAPI schema file
            zone_output_dir: Output directory for the zone

        Returns:
            GenerationResult with operation details
        """
        self.logger.info(f"Using datamodel-code-generator for {zone_name}")

        try:
            # Generate project and package names
            project_name = self.config.generators.python.project_name_template.format(
                zone=zone_name
            )

            # Build command for datamodel-code-generator
            cmd = [
                "datamodel-codegen",
                "--input",
                str(schema_path),
                "--input-file-type",
                "openapi",
                "--output",
                str(zone_output_dir / f"{project_name}.py"),
                "--target-python-version",
                "3.9",
                "--use-annotated",
                "--use-field-description",
                "--use-standard-collections",
                "--use-schema-description",
                "--use-union-operator",
                "--output-model-type",
                "pydantic_v2.BaseModel",
            ]

            success, output = run_command(" ".join(cmd), timeout=120)

            if success:
                # Check if file was generated
                generated_file = zone_output_dir / f"{project_name}.py"
                if generated_file.exists():
                    # Count generated files (just the main file for now)
                    files_generated = 1

                    # Enhance the generated client
                    self._enhance_datamodel_client(
                        zone_name, zone_output_dir, generated_file
                    )

                    self.logger.success(
                        f"Python client generated with datamodel-code-generator for {zone_name}: {files_generated} files"
                    )

                    return GenerationResult(
                        success=True,
                        zone_name=zone_name,
                        output_path=generated_file,
                        files_generated=files_generated,
                        error_message="",
                    )
                else:
                    error_msg = f"datamodel-code-generator did not create expected file: {generated_file}"
                    self.logger.error(error_msg)
                    return GenerationResult(
                        success=False,
                        zone_name=zone_name,
                        output_path=zone_output_dir,
                        files_generated=0,
                        error_message=error_msg,
                    )
            else:
                error_msg = f"datamodel-code-generator failed: {output}"
                self.logger.error(error_msg)

                # Save detailed error to log file
                log_file = zone_output_dir / f"error_{zone_name}.log"
                try:
                    with open(log_file, "w", encoding="utf-8") as f:
                        f.write(
                            f"=== Python Client Generation Error (datamodel-code-generator) ===\n"
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
            error_msg = f"datamodel-code-generator exception: {str(e)}"
            self.logger.error(error_msg)

            # Get full traceback with all details
            tb = traceback.format_exc()
            self.logger.error(f"Full traceback:\n{tb}")

            # Save detailed error log to file
            log_file = zone_output_dir / f"error_{zone_name}.log"
            try:
                with open(log_file, "w", encoding="utf-8") as f:
                    f.write(
                        f"=== Python Client Generation Error (datamodel-code-generator) ===\n"
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

    def _enhance_datamodel_client(
        self, zone_name: str, output_dir: Path, generated_file: Path
    ):
        """
        Enhance the generated datamodel-code-generator client with additional features.

        Args:
            zone_name: Name of the zone
            output_dir: Output directory for the zone
            generated_file: Path to the generated Python file
        """
        try:
            # Generate HTTP client using templates
            self._generate_http_client(zone_name, output_dir)

        except Exception as e:
            self.logger.warning(
                f"Failed to enhance datamodel client for {zone_name}: {e}"
            )

    def _generate_http_client(self, zone_name: str, output_dir: Path):
        """Generate HTTP client using Jinja2 templates."""
        try:
            import jinja2
            from datetime import datetime

            # Setup Jinja2 environment
            templates_dir = Path(__file__).parent / "templates"
            env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(str(templates_dir)),
                trim_blocks=True,
                lstrip_blocks=True,
            )

            # Get zone info from config
            zones = self.config.zones
            zone_info = zones.get(zone_name, {})

            # Prepare context for templates
            api_prefix = f"/{self.config.api_prefix}/"
            self.logger.info(f"Using api_prefix: {api_prefix} for zone {zone_name}")
            self.logger.info(f"Config api_prefix: {self.config.api_prefix}")
            
            context = {
                "zone_name": zone_name,
                "title": zone_info.get("title", f"{zone_name.title()} API"),
                "description": zone_info.get(
                    "description", f"HTTP client for {zone_name} zone"
                ),
                "apps": zone_info.get("apps", []),
                "generation_time": datetime.now().isoformat(),
                "version": self.config.version,
                "api_prefix": api_prefix,
            }
            
            self.logger.info(f"Template context api_prefix: {context['api_prefix']}")

            # Generate HTTP client
            http_client_template = env.get_template("python_http_client.py.j2")
            http_client_content = http_client_template.render(**context)
            
            http_client_file = output_dir / "http_client.py"
            with open(http_client_file, "w", encoding="utf-8") as f:
                f.write(http_client_content)

            # Generate example
            example_template = env.get_template("python_example.py.j2")
            example_content = example_template.render(**context)
            
            example_file = output_dir / "example.py"
            with open(example_file, "w", encoding="utf-8") as f:
                f.write(example_content)

            # Generate README
            readme_template = env.get_template("python_readme.md.j2")
            readme_content = readme_template.render(**context)
            
            readme_file = output_dir / "README.md"
            with open(readme_file, "w", encoding="utf-8") as f:
                f.write(readme_content)

            # Generate requirements.txt
            requirements_template = env.get_template("python_requirements.txt.j2")
            requirements_content = requirements_template.render(**context)
            
            requirements_file = output_dir / "requirements.txt"
            with open(requirements_file, "w", encoding="utf-8") as f:
                f.write(requirements_content)

            self.logger.debug(f"Generated HTTP client files for {zone_name}")

        except ImportError:
            self.logger.warning("Jinja2 not available, skipping HTTP client generation")
        except Exception as e:
            self.logger.warning(
                f"Failed to generate HTTP client for {zone_name}: {e}"
            )

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
            "available": self.is_datamodel_available(),
            "output_directory": str(self.output_dir),
            "enabled": self.config.generators.python.enabled,
            "project_name_template": self.config.generators.python.project_name_template,
            "package_name_template": self.config.generators.python.package_name_template,
            "overwrite": self.config.generators.python.overwrite,
            "fail_on_warning": self.config.generators.python.fail_on_warning,
            "custom_templates": self.config.generators.python.custom_templates,
        }
