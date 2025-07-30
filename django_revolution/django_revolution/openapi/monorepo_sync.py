"""
Multi-Monorepo Sync for Django Revolution

Synchronizes generated clients to multiple monorepo structures with temporary storage.
"""

import shutil
import json
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional, List

from ..config import DjangoRevolutionSettings, MonorepoConfig
from ..utils import Logger, ensure_directories, run_command


class MultiMonorepoSync:
    """Synchronizes generated clients to multiple monorepos with temporary storage."""

    def __init__(self, config: DjangoRevolutionSettings, logger: Logger):
        """
        Initialize multi-monorepo sync.

        Args:
            config: Django Revolution settings
            logger: Logger instance
        """
        self.config = config
        self.logger = logger
        self.temp_dir = Path(config.output.base_directory) / config.monorepo.temp_directory
        ensure_directories(self.temp_dir)

    def sync_typescript_client(
        self, zone_name: str, client_path: Path
    ) -> Dict[str, Any]:
        """
        Sync TypeScript client to all configured monorepos.

        Args:
            zone_name: Name of the zone
            client_path: Path to the generated client

        Returns:
            Sync operation results for all monorepos
        """
        if not self.config.monorepo.enabled:
            return {"success": False, "error": "Multi-monorepo sync disabled"}

        enabled_configs = self.config.monorepo.get_enabled_configurations()
        if not enabled_configs:
            return {"success": False, "error": "No enabled monorepo configurations"}

        results = {}
        
        # First, save to temporary directory
        temp_client_path = self._save_to_temp(zone_name, client_path, "typescript")
        if not temp_client_path:
            return {"success": False, "error": "Failed to save client to temp directory"}

        # Then sync to each monorepo
        for config in enabled_configs:
            result = self._sync_to_monorepo(zone_name, temp_client_path, config, "typescript")
            results[config.name] = result

        return {
            "success": any(r.get("success", False) for r in results.values()),
            "monorepo_results": results,
            "temp_path": str(temp_client_path)
        }

    def sync_python_client(self, zone_name: str, client_path: Path) -> Dict[str, Any]:
        """
        Sync Python client to all configured monorepos.

        Args:
            zone_name: Name of the zone
            client_path: Path to the generated client

        Returns:
            Sync operation results for all monorepos
        """
        if not self.config.monorepo.enabled:
            return {"success": False, "error": "Multi-monorepo sync disabled"}

        enabled_configs = self.config.monorepo.get_enabled_configurations()
        if not enabled_configs:
            return {"success": False, "error": "No enabled monorepo configurations"}

        results = {}
        
        # First, save to temporary directory
        temp_client_path = self._save_to_temp(zone_name, client_path, "python")
        if not temp_client_path:
            return {"success": False, "error": "Failed to save client to temp directory"}

        # Then sync to each monorepo
        for config in enabled_configs:
            result = self._sync_to_monorepo(zone_name, temp_client_path, config, "python")
            results[config.name] = result

        return {
            "success": any(r.get("success", False) for r in results.values()),
            "monorepo_results": results,
            "temp_path": str(temp_client_path)
        }

    def _save_to_temp(self, zone_name: str, client_path: Path, client_type: str) -> Optional[Path]:
        """
        Save client to temporary directory.

        Args:
            zone_name: Name of the zone
            client_path: Path to the generated client
            client_type: Type of client (typescript/python)

        Returns:
            Path to temporary client directory
        """
        try:
            temp_zone_dir = self.temp_dir / client_type / zone_name
            
            # Clean existing temp directory
            if temp_zone_dir.exists():
                shutil.rmtree(temp_zone_dir)
            
            temp_zone_dir.mkdir(parents=True, exist_ok=True)

            # Copy client to temp directory
            if client_path.is_file():
                shutil.copy2(client_path, temp_zone_dir / client_path.name)
            else:
                shutil.copytree(client_path, temp_zone_dir, dirs_exist_ok=True)

            self.logger.debug(f"Saved {client_type} client for {zone_name} to temp: {temp_zone_dir}")
            return temp_zone_dir

        except Exception as e:
            self.logger.error(f"Failed to save {client_type} client for {zone_name} to temp: {e}")
            return None

    def _sync_to_monorepo(
        self, zone_name: str, temp_client_path: Path, config: MonorepoConfig, client_type: str
    ) -> Dict[str, Any]:
        """
        Sync client from temp directory to specific monorepo.

        Args:
            zone_name: Name of the zone
            temp_client_path: Path to temporary client directory
            config: Monorepo configuration
            client_type: Type of client (typescript/python)

        Returns:
            Sync operation result
        """
        try:
            monorepo_path = Path(config.path)
            if not monorepo_path.exists():
                return {
                    "success": False,
                    "error": f"Monorepo path does not exist: {monorepo_path}",
                    "monorepo": config.name
                }

            target_path = monorepo_path / config.api_package_path / client_type / zone_name

            # Create target directory
            ensure_directories(target_path)

            # Copy from temp to monorepo
            if temp_client_path.is_file():
                shutil.copy2(temp_client_path, target_path / temp_client_path.name)
            else:
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(temp_client_path, target_path)

            # Update monorepo files
            self._update_monorepo_files(zone_name, target_path, client_type, config)

            # Run monorepo commands
            commands_run = self._run_monorepo_commands(target_path, client_type, config)

            self.logger.success(
                f"Synced {client_type} client for {zone_name} to monorepo {config.name}"
            )

            return {
                "success": True,
                "monorepo": config.name,
                "target_path": str(target_path),
                "commands_run": commands_run
            }

        except Exception as e:
            error_msg = f"Failed to sync {client_type} client for {zone_name} to monorepo {config.name}: {e}"
            self.logger.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "monorepo": config.name
            }

    def _update_monorepo_files(
        self, zone_name: str, target_path: Path, client_type: str, config: MonorepoConfig
    ):
        """Update monorepo-specific files."""
        if client_type == "typescript":
            self._update_typescript_monorepo_files(zone_name, target_path, config)
        elif client_type == "python":
            self._update_python_monorepo_files(zone_name, target_path, config)

    def _update_typescript_monorepo_files(self, zone_name: str, target_path: Path, config: MonorepoConfig):
        """Update TypeScript monorepo files."""
        try:
            # Update package.json if exists
            package_json = target_path / "package.json"
            if package_json.exists():
                with open(package_json, "r") as f:
                    package_data = json.load(f)
                
                # Update package name to include monorepo context
                package_data["name"] = f"@{config.name}/{zone_name}"
                package_data["version"] = self.config.version
                
                with open(package_json, "w") as f:
                    json.dump(package_data, f, indent=2)

            # Create or update index.ts
            index_ts = target_path / "index.ts"
            if not index_ts.exists():
                index_content = f"""/**
 * {zone_name.title()} API Client
 * Generated for monorepo: {config.name}
 */

export * from './sdk.gen';
export * from './types.gen';
export * from './client.gen';

// Re-export main client for convenience
export {{ client as default }} from './client.gen';
"""
                with open(index_ts, "w") as f:
                    f.write(index_content)

        except Exception as e:
            self.logger.warning(f"Failed to update TypeScript monorepo files for {zone_name}: {e}")

    def _update_python_monorepo_files(self, zone_name: str, target_path: Path, config: MonorepoConfig):
        """Update Python monorepo files."""
        try:
            # Update __init__.py if exists
            init_py = target_path / "__init__.py"
            if init_py.exists():
                init_content = f'''"""
{zone_name.title()} API Client - Python Package
Generated for monorepo: {config.name}
"""

from .{zone_name}_client.client import (
    {zone_name.title()}Client,
    {zone_name.title()}Config,
    {zone_name.title()}Response,
    {zone_name}_client
)

__version__ = "{self.config.version}"
__author__ = "Unrealos"
__description__ = "{zone_name.title()} API Client for {config.name} monorepo"

__all__ = [
    "{zone_name.title()}Client",
    "{zone_name.title()}Config", 
    "{zone_name.title()}Response",
    "{zone_name}_client"
]
'''
                with open(init_py, "w") as f:
                    f.write(init_content)

        except Exception as e:
            self.logger.warning(f"Failed to update Python monorepo files for {zone_name}: {e}")

    def _run_monorepo_commands(self, target_path: Path, client_type: str, config: MonorepoConfig) -> List[str]:
        """Run monorepo-specific commands."""
        commands_run = []
        
        try:
            monorepo_path = Path(config.path)
            
            # Check package.json for packageManager field first
            package_json = monorepo_path / "package.json"
            if package_json.exists():
                with open(package_json, "r") as f:
                    package_data = json.load(f)
                    package_manager = package_data.get("packageManager", "")
                    
                    # Only support pnpm
                    if "pnpm" in package_manager:
                        # Run pnpm install
                        success, output = run_command("pnpm install", cwd=monorepo_path, timeout=300)
                        if success:
                            commands_run.append("pnpm install")
                        else:
                            self.logger.warning(f"Failed to run pnpm install in {config.name}: {output}")
                        return commands_run
            
            # Fallback: Check for pnpm workspace
            pnpm_workspace = monorepo_path / "pnpm-workspace.yaml"
            if pnpm_workspace.exists():
                # Run pnpm install
                success, output = run_command("pnpm install", cwd=monorepo_path, timeout=300)
                if success:
                    commands_run.append("pnpm install")
                else:
                    self.logger.warning(f"Failed to run pnpm install in {config.name}: {output}")
                return commands_run

        except Exception as e:
            self.logger.warning(f"Failed to run monorepo commands for {config.name}: {e}")

        return commands_run

    def sync_all_clients(self, clients_dir: Path) -> Dict[str, Any]:
        """
        Sync all generated clients to all monorepos.

        Args:
            clients_dir: Base clients directory

        Returns:
            Overall sync operation results
        """
        if not self.config.monorepo.enabled:
            return {"success": False, "error": "Multi-monorepo sync disabled"}

        self.logger.info("Starting multi-monorepo sync for all clients...")

        # Get all zone directories
        ts_clients_dir = clients_dir / "typescript"
        py_clients_dir = clients_dir / "python"

        sync_results = {
            "typescript": {},
            "python": {},
            "summary": {"total_zones": 0, "successful": 0, "failed": 0}
        }

        # Sync TypeScript clients
        if ts_clients_dir.exists():
            for zone_dir in ts_clients_dir.iterdir():
                if zone_dir.is_dir():
                    zone_name = zone_dir.name
                    sync_results["summary"]["total_zones"] += 1
                    
                    result = self.sync_typescript_client(zone_name, zone_dir)
                    sync_results["typescript"][zone_name] = result
                    
                    if result.get("success"):
                        sync_results["summary"]["successful"] += 1
                    else:
                        sync_results["summary"]["failed"] += 1

        # Sync Python clients
        if py_clients_dir.exists():
            for zone_dir in py_clients_dir.iterdir():
                if zone_dir.is_dir():
                    zone_name = zone_dir.name
                    
                    result = self.sync_python_client(zone_name, zone_dir)
                    sync_results["python"][zone_name] = result

        self.logger.info(
            f"Multi-monorepo sync completed: {sync_results['summary']['successful']} successful, "
            f"{sync_results['summary']['failed']} failed"
        )

        return sync_results

    def sync_all(self) -> Dict[str, Any]:
        """
        Sync all clients to all monorepos.

        Returns:
            Dictionary with sync results
        """
        if not self.config.monorepo.enabled:
            return {"success": False, "error": "Multi-monorepo sync disabled"}

        clients_dir = Path(self.config.output.base_directory) / self.config.output.clients_directory
        return self.sync_all_clients(clients_dir)

    def sync_zone(self, zone_name: str) -> bool:
        """
        Sync a specific zone to all monorepos.

        Args:
            zone_name: Name of the zone to sync

        Returns:
            bool: True if sync was successful for at least one monorepo
        """
        if not self.config.monorepo.enabled:
            return False

        clients_dir = Path(self.config.output.base_directory) / self.config.output.clients_directory
        
        # Try TypeScript first
        ts_client_path = clients_dir / "typescript" / zone_name
        if ts_client_path.exists():
            result = self.sync_typescript_client(zone_name, ts_client_path)
            return result.get("success", False)

        # Try Python if TypeScript doesn't exist
        py_client_path = clients_dir / "python" / zone_name
        if py_client_path.exists():
            result = self.sync_python_client(zone_name, py_client_path)
            return result.get("success", False)

        return False

    def generate_consolidated_index(self, zones: List[str]):
        """
        Generate consolidated index.ts for all zones in all monorepos.

        Args:
            zones: List of zone names
        """
        if not self.config.monorepo.enabled:
            return

        enabled_configs = self.config.monorepo.get_enabled_configurations()
        
        for config in enabled_configs:
            try:
                monorepo_path = Path(config.path)
                api_package_path = monorepo_path / config.api_package_path / "typescript"
                
                if not api_package_path.exists():
                    continue

                # Generate consolidated index for this monorepo
                self._generate_monorepo_index(api_package_path, zones, config)

            except Exception as e:
                self.logger.error(f"Failed to generate consolidated index for {config.name}: {e}")

    def _generate_monorepo_index(self, api_package_path: Path, zones: List[str], config: MonorepoConfig):
        """Generate consolidated index.ts for a specific monorepo."""
        try:
            import jinja2
            from datetime import datetime

            def camelcase(name: str) -> str:
                """Convert snake_case to camelCase."""
                parts = name.split('_')
                return parts[0] + ''.join(part.title() for part in parts[1:])

            # Setup Jinja2 environment
            templates_dir = Path(__file__).parent / "templates"
            env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(str(templates_dir)),
                trim_blocks=True,
                lstrip_blocks=True,
            )

            # Prepare context
            context = {
                "zones": zones,
                "generation_time": datetime.now().isoformat(),
                "camelcase": camelcase,
                "monorepo_name": config.name,
            }

            # Render template
            template = env.get_template("index_consolidated.ts.j2")
            index_content = template.render(**context)

            # Write consolidated index.ts
            with open(api_package_path / "index.ts", "w", encoding="utf-8") as f:
                f.write(index_content)

            self.logger.success(
                f"Consolidated index.ts generated for monorepo {config.name} with zones: {zones}"
            )

        except ImportError:
            self.logger.warning(
                "Jinja2 not available, skipping consolidated index generation"
            )
        except Exception as e:
            self.logger.error(f"Failed to generate consolidated index.ts for {config.name}: {e}")

    def get_status(self) -> Dict[str, Any]:
        """
        Get multi-monorepo sync status.

        Returns:
            Dictionary with status information
        """
        enabled_configs = self.config.monorepo.get_enabled_configurations()
        
        status = {
            "enabled": self.config.monorepo.enabled,
            "total_configurations": len(self.config.monorepo.configurations),
            "enabled_configurations": len(enabled_configs),
            "configurations": []
        }

        for config in self.config.monorepo.configurations:
            config_status = {
                "name": config.name,
                "enabled": config.enabled,
                "path": config.path,
                "api_package_path": config.api_package_path,
                "exists": Path(config.path).exists() if config.enabled else False
            }
            status["configurations"].append(config_status)

        return status

    def clean_temp_directory(self) -> bool:
        """
        Clean temporary directory.

        Returns:
            bool: True if cleaning successful
        """
        try:
            if self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                self.logger.success("Temporary monorepo sync directory cleaned")
            return True
        except Exception as e:
            self.logger.error(f"Failed to clean temporary directory: {e}")
            return False 