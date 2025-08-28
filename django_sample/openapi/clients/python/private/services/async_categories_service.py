import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def categories_list(
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedCategoryList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedCategoryList(**response.json())
        if response.json() is not None
        else PaginatedCategoryList()
    )


async def categories_create(
    data: Category, api_config_override: Optional[APIConfig] = None
) -> Category:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "post",
            httpx.URL(path),
            headers=headers,
            params=query_params,
            json=data.dict(),
        )

    if response.status_code != 201:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Category(**response.json()) if response.json() is not None else Category()


async def categories_products_list(
    category_id: int,
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedProductList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedProductList(**response.json())
        if response.json() is not None
        else PaginatedProductList()
    )


async def categories_products_create(
    category_id: int, data: Product, api_config_override: Optional[APIConfig] = None
) -> Product:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "post",
            httpx.URL(path),
            headers=headers,
            params=query_params,
            json=data.dict(),
        )

    if response.status_code != 201:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Product(**response.json()) if response.json() is not None else Product()


async def categories_products_retrieve(
    category_id: int, id: int, api_config_override: Optional[APIConfig] = None
) -> Product:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Product(**response.json()) if response.json() is not None else Product()


async def categories_products_update(
    category_id: int,
    id: int,
    data: Product,
    api_config_override: Optional[APIConfig] = None,
) -> Product:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "put",
            httpx.URL(path),
            headers=headers,
            params=query_params,
            json=data.dict(),
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Product(**response.json()) if response.json() is not None else Product()


async def categories_products_destroy(
    category_id: int, id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 204:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return None


async def categories_products_partial_update(
    category_id: int,
    id: int,
    data: PatchedProduct,
    api_config_override: Optional[APIConfig] = None,
) -> Product:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "patch",
            httpx.URL(path),
            headers=headers,
            params=query_params,
            json=data.dict(),
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Product(**response.json()) if response.json() is not None else Product()


async def categories_products_order_items_list(
    category_id: int,
    id: int,
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedOrderItemList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/{id}/order_items/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedOrderItemList(**response.json())
        if response.json() is not None
        else PaginatedOrderItemList()
    )


async def categories_products_by_category_list(
    category_id: int,
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedProductList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/by_category/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedProductList(**response.json())
        if response.json() is not None
        else PaginatedProductList()
    )


async def categories_products_low_stock_list(
    category_id: int,
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedProductList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{category_id}/products/low_stock/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedProductList(**response.json())
        if response.json() is not None
        else PaginatedProductList()
    )


async def categories_retrieve(
    id: int, api_config_override: Optional[APIConfig] = None
) -> Category:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Category(**response.json()) if response.json() is not None else Category()


async def categories_update(
    id: int, data: Category, api_config_override: Optional[APIConfig] = None
) -> Category:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "put",
            httpx.URL(path),
            headers=headers,
            params=query_params,
            json=data.dict(),
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Category(**response.json()) if response.json() is not None else Category()


async def categories_destroy(
    id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 204:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return None


async def categories_partial_update(
    id: int, data: PatchedCategory, api_config_override: Optional[APIConfig] = None
) -> Category:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "patch",
            httpx.URL(path),
            headers=headers,
            params=query_params,
            json=data.dict(),
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return Category(**response.json()) if response.json() is not None else Category()


async def categories_products_list_2(
    id: int,
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedProductList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/{id}/products/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedProductList(**response.json())
        if response.json() is not None
        else PaginatedProductList()
    )


async def categories_active_list(
    ordering: Optional[str] = None,
    page: Optional[int] = None,
    search: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PaginatedCategoryList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/private_api/categories/active/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "ordering": ordering,
        "page": page,
        "search": search,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with httpx.AsyncClient(
        base_url=base_path, verify=api_config.verify
    ) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code, f" failed with status code: {response.status_code}"
        )

    return (
        PaginatedCategoryList(**response.json())
        if response.json() is not None
        else PaginatedCategoryList()
    )
