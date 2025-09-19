# Contributing to Django Revolution

Thank you for your interest in contributing to Django Revolution! This document provides guidelines and information for contributors.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- Node.js 18+ (for TypeScript generation)
- Git

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

   ```bash
   git clone https://github.com/YOUR_USERNAME/django-revolution.git
   cd django-revolution
   ```

3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/markolofsen/django-revolution.git
   ```

## Development Setup

### Install Dependencies

```bash
# Install Python dependencies
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Install Node.js dependencies (if working on TypeScript generation)
npm install
```

### Run Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=django_revolution

# Run specific test file
pytest tests/test_config.py
```

### Development Environment

```bash
# Create a test Django project
cd django_sample
python manage.py migrate
python manage.py runserver

# Test Django Revolution commands
python manage.py revolution --status
python manage.py revolution --list-zones
```

## Code Style

### Python

We follow PEP 8 with some modifications:

- Line length: 88 characters (Black default)
- Use Black for code formatting
- Use isort for import sorting
- Use flake8 for linting

```bash
# Format code
black django_revolution/
isort django_revolution/

# Check code style
flake8 django_revolution/
```

### TypeScript/JavaScript

- Use Prettier for formatting
- Follow ESLint rules
- Use TypeScript for type safety

```bash
# Format TypeScript code
npx prettier --write clients/typescript/

# Check TypeScript
npx tsc --noEmit
```

## Testing

### Writing Tests

- Write tests for all new features
- Use pytest for testing
- Aim for high test coverage
- Test both success and error cases

### Test Structure

```python
# tests/test_feature.py
import pytest
from django_revolution.feature import Feature

class TestFeature:
    def test_feature_works(self):
        feature = Feature()
        result = feature.do_something()
        assert result == expected_value

    def test_feature_handles_errors(self):
        feature = Feature()
        with pytest.raises(ValueError):
            feature.do_something_with_invalid_input()
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests in parallel
pytest -n auto

# Run tests with verbose output
pytest -v

# Run tests and generate coverage report
pytest --cov=django_revolution --cov-report=html
```

## Documentation

### Updating Documentation

1. **Documentation Structure:**

   - `docs/` - Main documentation (Markdown)
   - `django_revolution/` - Code documentation (docstrings)

2. **Documentation Guidelines:**

   - Write clear, concise documentation
   - Include code examples
   - Update both user and developer docs
   - Use proper Markdown formatting

3. **Building Documentation:**
   ```bash
   # Build Jekyll docs locally
   cd docs
   bundle exec jekyll serve
   ```

### Code Documentation

- Use Google-style docstrings
- Document all public functions and classes
- Include type hints
- Provide usage examples

```python
def generate_clients(zones: List[str] = None) -> Dict[str, Any]:
    """Generate TypeScript and Python clients for specified zones.

    Args:
        zones: List of zone names to generate clients for.
               If None, generates for all zones.

    Returns:
        Dictionary with generation results and metadata.

    Raises:
        ValueError: If zone configuration is invalid.
        RuntimeError: If client generation fails.

    Example:
        >>> result = generate_clients(['public', 'admin'])
        >>> print(result['status'])
        'success'
    """
    pass
```

## Pull Request Process

### Before Submitting

1. **Create a feature branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**

   - Write code following our style guidelines
   - Add tests for new functionality
   - Update documentation
   - Update CHANGELOG.md if needed

3. **Test your changes:**

   ```bash
   # Run tests
   pytest

   # Check code style
   black --check django_revolution/
   flake8 django_revolution/

   # Test Django Revolution commands
   cd django_sample
   python manage.py revolution --status
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

### Submitting a Pull Request

1. **Push your branch:**

   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request:**

   - Use the PR template
   - Provide a clear description
   - Link related issues
   - Include screenshots if UI changes

3. **PR Checklist:**
   - [ ] Code follows style guidelines
   - [ ] Tests pass
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated
   - [ ] No breaking changes (or documented)

### PR Review Process

1. **Automated Checks:**

   - Tests must pass
   - Code coverage maintained
   - Style checks pass

2. **Manual Review:**

   - At least one maintainer must approve
   - Address all review comments
   - Update PR if requested

3. **Merging:**
   - Squash commits if requested
   - Delete feature branch after merge

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Environment Information:**

   - Python version
   - Django version
   - Django Revolution version
   - Operating system

2. **Steps to Reproduce:**

   - Clear, step-by-step instructions
   - Minimal example code
   - Expected vs actual behavior

3. **Additional Information:**
   - Error messages and stack traces
   - Screenshots if applicable
   - Related issues

### Issue Template

```markdown
**Environment:**

- Python: 3.11.0
- Django: 4.2.0
- Django Revolution: 1.0.6
- OS: macOS 13.0

**Steps to reproduce:**

1. Install Django Revolution
2. Configure zones in settings.py
3. Run `python manage.py revolution`
4. See error: [paste error here]

**Expected behavior:**
[Describe what should happen]

**Actual behavior:**
[Describe what actually happens]

**Additional information:**
[Any other relevant details]
```

## Feature Requests

### Suggesting Features

1. **Check existing issues** to avoid duplicates
2. **Provide clear description** of the feature
3. **Explain use cases** and benefits
4. **Consider implementation** complexity

### Feature Request Template

```markdown
**Feature Description:**
[Clear description of the feature]

**Use Cases:**

- [Use case 1]
- [Use case 2]

**Benefits:**
[Why this feature would be valuable]

**Implementation Ideas:**
[Optional: thoughts on how to implement]

**Additional Context:**
[Any other relevant information]
```

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Use welcoming and inclusive language
- Be collaborative and constructive
- Focus on what is best for the community

### Enforcement

- Unacceptable behavior will not be tolerated
- Maintainers will remove, edit, or reject comments/commits/PRs
- Violations may result in temporary or permanent ban

## Getting Help

### Communication Channels

- **GitHub Issues:** For bugs and feature requests
- **GitHub Discussions:** For questions and general discussion
- **Pull Requests:** For code contributions

### Resources

- [Documentation](https://revolution.reforms.ai/)
- [API Reference](https://revolution.reforms.ai/api-reference/)
- [Examples](https://github.com/markolofsen/django-revolution/tree/main/django_sample)

## Recognition

### Contributors

All contributors will be recognized in:

- [CONTRIBUTORS.md](CONTRIBUTORS.md)
- Release notes
- Project documentation

### Types of Contributions

We welcome all types of contributions:

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Tests
- 🔧 Tooling and infrastructure
- 💡 Ideas and feedback

Thank you for contributing to Django Revolution! 🚀
