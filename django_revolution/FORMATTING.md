# 🎨 Auto-Formatting in Django Revolution

Django Revolution automatically formats generated client code using industry-standard tools to ensure consistent, readable output.

## 📋 Overview

After generating TypeScript and Python clients, Django Revolution automatically formats the code using:

- **Python**: [Black](https://black.readthedocs.io/) - The uncompromising Python code formatter
- **TypeScript**: [Prettier](https://prettier.io/) - An opinionated code formatter

## ⚙️ Configuration

### Enabling/Disabling Auto-Formatting

Auto-formatting is enabled by default but can be controlled via configuration:

```python
from django_revolution import DjangoRevolutionSettings

config = DjangoRevolutionSettings(
    generators={
        "typescript": {
            "auto_format": True,  # Enable TypeScript formatting
        },
        "python": {
            "auto_format": True,  # Enable Python formatting
        }
    }
)
```

### Configuration Files

#### TypeScript/JavaScript - Prettier

Configuration file: `django_revolution/.prettierrc`

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "lf",
  "quoteProps": "as-needed",
  "jsxSingleQuote": true,
  "bracketSameLine": false
}
```

#### Python - Black

Configuration in `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ["py39"]
include = '\.pyi?$'
extend-exclude = '''
/(
  \.eggs
  | \.git
  | \.mypy_cache
  | \.venv
  | build
  | dist
  | openapi
  | generated
)/
'''
```

## 🚀 Usage

### Automatic Formatting

When you generate clients, formatting happens automatically:

```python
from django_revolution import quick_generate

# Auto-formatting is applied to all generated files
results = quick_generate(
    zones=["api", "admin"],
    typescript=True,
    python=True
)
```

### Manual Formatting

You can also format files manually using the provided npm scripts:

```bash
# Navigate to django_revolution directory
cd django_revolution/

# Format TypeScript files
npm run format:ts

# Format Python files  
npm run format:python

# Format all files
npm run format:all

# Check formatting without changing files
npm run format:check
npm run lint:ts
```

## 📦 Dependencies

### Python Dependencies

Auto-formatting requires Black to be installed:

```bash
# Install with formatting support
pip install django-revolution[formatting]

# Or install Black separately
pip install black>=21.0
```

### Node.js Dependencies

TypeScript formatting requires Prettier and Node.js:

```bash
# Install Node.js dependencies
cd django_revolution/
npm install

# Or install globally
npm install -g prettier @hey-api/openapi-ts
```

## 🔧 Troubleshooting

### Black Not Available

If you see "Black not available, skipping Python formatting":

```bash
pip install black>=21.0
# or
pip install django-revolution[formatting]
```

### Prettier Not Available

If you see "Prettier not available, skipping TypeScript formatting":

```bash
npm install -g prettier
# or
cd django_revolution/ && npm install
```

### Formatting Fails

If formatting fails but generation succeeds, check:

1. **File permissions**: Ensure generated files are writable
2. **Syntax errors**: Generated code may have syntax issues
3. **Tool versions**: Ensure compatible versions of Black/Prettier

## 📝 Customization

### Custom Prettier Configuration

Modify `django_revolution/.prettierrc` to customize TypeScript formatting:

```json
{
  "printWidth": 120,
  "tabWidth": 4,
  "singleQuote": false
}
```

### Custom Black Configuration

Modify `pyproject.toml` to customize Python formatting:

```toml
[tool.black]
line-length = 100
target-version = ["py310"]
```

### Disable Formatting for Specific Files

Add patterns to `.prettierignore`:

```
# Ignore generated API files
*.gen.ts
*.gen.js

# Ignore specific directories
generated/
openapi/
```

## 🎯 Best Practices

1. **Keep formatting enabled** - Consistent code style improves readability
2. **Commit configuration files** - Include `.prettierrc` and `pyproject.toml` in version control
3. **Use pre-commit hooks** - Set up automatic formatting in your development workflow
4. **Test formatting tools** - Ensure Black and Prettier are available in your environment

## 🔍 Debugging

Enable debug logging to see formatting details:

```python
import logging
logging.getLogger('django_revolution').setLevel(logging.DEBUG)

# You'll see messages like:
# 🎨 Formatting 15 TypeScript files...
# ✅ TypeScript files formatted successfully
```

## 📊 Performance

Formatting adds minimal overhead to generation:

- **Python formatting**: ~1-2 seconds for typical client
- **TypeScript formatting**: ~2-3 seconds for typical client
- **Total impact**: Usually <10% of total generation time

Formatting can be disabled for faster generation in development environments.
