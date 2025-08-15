#!/usr/bin/env python3
"""
Generate requirements.txt from pyproject.toml

This script automatically generates requirements.txt files for different environments
based on the dependencies defined in pyproject.toml.
"""

import sys
import tomllib
from pathlib import Path
from typing import Dict, List


def parse_pyproject_toml(pyproject_path: Path) -> Dict:
    """Parse pyproject.toml file."""
    try:
        with open(pyproject_path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        print(f"❌ Failed to parse pyproject.toml: {e}")
        sys.exit(1)


def extract_dependencies(project_data: Dict) -> List[str]:
    """Extract main dependencies from project data."""
    dependencies = project_data.get("project", {}).get("dependencies", [])

    # Convert to requirements.txt format
    requirements = []
    for dep in dependencies:
        # Handle different dependency formats
        if isinstance(dep, str):
            requirements.append(dep)
        elif isinstance(dep, dict):
            # Handle dependency with extras
            name = dep.get("name", "")
            version = dep.get("version", "")
            if name and version:
                requirements.append(f"{name}{version}")
            elif name:
                requirements.append(name)

    return requirements


def extract_dev_dependencies(project_data: Dict) -> List[str]:
    """Extract development dependencies from project data."""
    optional_deps = project_data.get("project", {}).get("optional-dependencies", {})
    dev_deps = optional_deps.get("dev", [])

    # Convert to requirements.txt format
    requirements = []
    for dep in dev_deps:
        if isinstance(dep, str):
            requirements.append(dep)
        elif isinstance(dep, dict):
            name = dep.get("name", "")
            version = dep.get("version", "")
            if name and version:
                requirements.append(f"{name}{version}")
            elif name:
                requirements.append(name)

    return requirements


def write_requirements_file(
    requirements: List[str], output_path: Path, header: str = ""
):
    """Write requirements to file."""
    with open(output_path, "w", encoding="utf-8") as f:
        if header:
            f.write(f"# {header}\n")
            f.write("# Generated automatically from pyproject.toml\n")
            f.write("# Do not edit manually!\n\n")

        for req in sorted(requirements):
            f.write(f"{req}\n")


def generate_requirements_files() -> bool:
    """Generate all requirements files."""
    base_path = Path(__file__).parent.parent
    pyproject_path = base_path / "pyproject.toml"

    if not pyproject_path.exists():
        print(f"❌ pyproject.toml not found at {pyproject_path}")
        return False

    try:
        project_data = parse_pyproject_toml(pyproject_path)
    except Exception as e:
        print(f"❌ Failed to parse pyproject.toml: {e}")
        return False

    # Extract dependencies
    main_deps = extract_dependencies(project_data)
    dev_deps = extract_dev_dependencies(project_data)

    # Generate requirements.txt (main dependencies only)
    requirements_path = base_path / "requirements.txt"
    write_requirements_file(
        main_deps, requirements_path, "Main dependencies for UnrealOn SDK"
    )
    print(f"✅ Generated {requirements_path}")

    # Generate requirements-dev.txt (main + dev dependencies)
    requirements_dev_path = base_path / "requirements-dev.txt"
    all_deps = main_deps + dev_deps
    write_requirements_file(
        all_deps,
        requirements_dev_path,
        "Development dependencies for UnrealOn SDK (includes main deps)",
    )
    print(f"✅ Generated {requirements_dev_path}")

    # Generate requirements-minimal.txt (core dependencies only)
    core_deps = [
        "pydantic>=2.0.0",
        "websockets>=10.0",
        "aiohttp>=3.8.0",
    ]
    requirements_minimal_path = base_path / "requirements-minimal.txt"
    write_requirements_file(
        core_deps,
        requirements_minimal_path,
        "Minimal dependencies for UnrealOn SDK (core only)",
    )
    print(f"✅ Generated {requirements_minimal_path}")

    # Print summary
    print(f"\n📊 Summary:")
    print(f"  Main dependencies: {len(main_deps)}")
    print(f"  Dev dependencies: {len(dev_deps)}")
    print(f"  Total dependencies: {len(all_deps)}")

    return True


if __name__ == "__main__":
    sys.exit(0 if generate_requirements_files() else 1)