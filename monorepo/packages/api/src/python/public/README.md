# Public API Client

Generated Python HTTP client for public zone using Django Revolution.

## Features

- ✅ **Full HTTP Client**: Complete HTTP client with retry logic and error handling
- ✅ **Generated Models**: Pydantic models for all API endpoints
- ✅ **Type Safety**: Full type hints and validation
- ✅ **Authentication**: Built-in token-based authentication
- ✅ **Retry Logic**: Automatic retry on network errors
- ✅ **Response Wrapping**: Clean response objects with status checking
- ✅ **Specific API Methods**: Convenient methods for each endpoint

## Installation

```bash
pip install pydantic requests
```

## Quick Start

```python
from http_client import public_client

# Create client
client = public_client("http://localhost:8000")

# Use specific API methods
posts = client.get_posts()
if posts.is_success():
    print(f"Found {len(posts.data['results'])} posts")
```

## Usage

### Basic API Calls

```python
from http_client import public_client

# Initialize client
client = public_client("http://localhost:8000")

# GET request
response = client.get("public/")
if response.is_success():
    data = response.data
    print(f"Response: {data}")

# POST request
data = {"name": "new_item", "description": "Test item"}
response = client.post("public/items/", data=data)
if response.is_success():
    print("Item created successfully")

# PUT request
update_data = {"description": "Updated description"}
response = client.put("public/items/1/", data=update_data)

# DELETE request
response = client.delete("public/items/1/")
```

### Specific API Methods

The client provides convenient methods for each endpoint:

#### Posts API

```python
# Get all posts with filtering and pagination
posts = client.get_posts(
    ordering="-created_at",  # Sort by newest first
    page=1,                  # Page number
    search="python"          # Search term
)

# Get only published posts
published_posts = client.get_published_posts(ordering="-created_at")

# Get posts by specific author
author_posts = client.get_posts_by_author(author_id=1)

# Create a new post
new_post = client.create_post({
    "title": "My New Post",
    "content": "Post content here",
    "author_id": 1,
    "published": False
})

# Get a specific post
post = client.get_post(post_id=1)

# Update a post (full update)
updated_post = client.update_post(post_id=1, post_data={
    "title": "Updated Title",
    "content": "Updated content",
    "author_id": 1,
    "published": True
})

# Partially update a post
patched_post = client.patch_post(post_id=1, post_data={
    "title": "New Title Only"
})

# Publish/unpublish a post
client.publish_post(post_id=1)
client.unpublish_post(post_id=1)

# Delete a post
client.delete_post(post_id=1)
```

### Using Generated Models

```python
from models import *

# Create model instance (adjust based on your actual models)
# Example: Create a request model
if 'Post' in globals():
    post_request = Post(
        title="Test Post",
        content="Test content",
        author_id=1,
        published=True
    )

    # POST with model data
    response = client.create_post(post_request.model_dump())

    # Parse response into model
    if response.is_success():
        post = Post(**response.data)
        print(f"Created post: {post.title}")
```

### Authentication

```python
# Set authentication token
client.set_auth_token("your-jwt-token-here")

# Make authenticated request
response = client.get("public/protected-endpoint/")

# Clear token when done
client.clear_auth_token()
```

### Error Handling

```python
try:
    response = client.get_posts()
    if response.is_success():
        print("Request successful")
    else:
        print(f"Request failed: {response.status_code}")
        print(f"Error: {response.data}")
except Exception as e:
    print(f"Network error: {e}")
```

### Advanced Configuration

```python
from http_client import PublicConfig, PublicClient

# Custom configuration
config = PublicConfig(
    base_url="https://api.example.com",
    api_prefix="/api/v1/",
    timeout=60,
    max_retries=5,
    headers={"X-Custom-Header": "value"},
    auth_token="your-token"
)

# Create client with custom config
client = PublicClient(config)
```

## API Endpoints

This client provides access to all endpoints in the public zone:

### Posts Endpoints

- `GET /api/public_api/posts/` - List all posts
- `POST /api/public_api/posts/` - Create a new post
- `GET /api/public_api/posts/{id}/` - Get specific post
- `PUT /api/public_api/posts/{id}/` - Update post (full)
- `PATCH /api/public_api/posts/{id}/` - Update post (partial)
- `DELETE /api/public_api/posts/{id}/` - Delete post
- `POST /api/public_api/posts/{id}/publish/` - Publish post
- `POST /api/public_api/posts/{id}/unpublish/` - Unpublish post
- `GET /api/public_api/posts/by_author/` - Get posts by author
- `GET /api/public_api/posts/published/` - Get published posts only

## Generated Models

The following Pydantic models are available in `models.py`:

- `User` - User model with fields: id, username, email, first_name, last_name, date_joined
- `Post` - Post model with fields: id, title, content, author, author_id, published, created_at
- `PatchedPost` - Partial post update model
- `PaginatedPostList` - Paginated response wrapper

## Configuration

### PublicConfig

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `base_url` | str | "http://localhost:8000" | Base URL for API |
| `api_prefix` | str | "/api/" | API path prefix |
| `timeout` | int | 30 | Request timeout in seconds |
| `max_retries` | int | 3 | Maximum retry attempts |
| `headers` | Dict[str, str] | {} | Custom headers |
| `auth_token` | str | None | Authentication token |

### PublicResponse

| Property | Type | Description |
|----------|------|-------------|
| `response` | requests.Response | Raw requests response |
| `data` | Any | Parsed response data |
| `status_code` | int | HTTP status code |
| `headers` | Dict[str, str] | Response headers |
| `url` | str | Request URL |

## Development

This client was generated by Django Revolution. To regenerate:

```bash
python manage.py revolution --generate --zones public
```

## License

Generated by Django Revolution. 