import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def api_public_api_posts_list(
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedPostList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {"ordering": ordering, "page": page, "search": search}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return PaginatedPostList(**response.json()) if response.json() is not None else PaginatedPostList()


async def api_public_api_posts_create(data: Post, api_config_override: Optional[APIConfig] = None) -> Post:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 201:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Post(**response.json()) if response.json() is not None else Post()


async def api_public_api_posts_retrieve(id: int, api_config_override: Optional[APIConfig] = None) -> Post:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Post(**response.json()) if response.json() is not None else Post()


async def api_public_api_posts_update(id: int, data: Post, api_config_override: Optional[APIConfig] = None) -> Post:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("put", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Post(**response.json()) if response.json() is not None else Post()


async def api_public_api_posts_destroy(id: int, api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 204:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


async def api_public_api_posts_partial_update(
    id: int, data: PatchedPost, api_config_override: Optional[APIConfig] = None
) -> Post:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "patch", httpx.URL(path), headers=headers, params=query_params, json=data.dict()
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Post(**response.json()) if response.json() is not None else Post()


async def api_public_api_posts_publish_create(
    id: int, data: Post, api_config_override: Optional[APIConfig] = None
) -> Post:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/{id}/publish/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Post(**response.json()) if response.json() is not None else Post()


async def api_public_api_posts_unpublish_create(
    id: int, data: Post, api_config_override: Optional[APIConfig] = None
) -> Post:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/{id}/unpublish/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Post(**response.json()) if response.json() is not None else Post()


async def api_public_api_posts_by_author_list(
    author_id: Optional[int] = None,
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedPostList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/by_author/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {"author_id": author_id, "ordering": ordering, "page": page, "search": search}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return PaginatedPostList(**response.json()) if response.json() is not None else PaginatedPostList()


async def api_public_api_posts_published_list(
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedPostList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/public_api/posts/published/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {"ordering": ordering, "page": page, "search": search}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return PaginatedPostList(**response.json()) if response.json() is not None else PaginatedPostList()
