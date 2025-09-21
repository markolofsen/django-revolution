from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category import Category
from ...models.category_request import CategoryRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        CategoryRequest,
        CategoryRequest,
        CategoryRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/private_api/categories/{id}/",
    }

    if isinstance(body, CategoryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CategoryRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CategoryRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Category]:
    if response.status_code == 200:
        response_200 = Category.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Category]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        CategoryRequest,
        CategoryRequest,
        CategoryRequest,
    ],
) -> Response[Category]:
    """ViewSet for Category model with nested routing and drf-spectacular documentation.

    Args:
        id (int):
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Category]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        CategoryRequest,
        CategoryRequest,
        CategoryRequest,
    ],
) -> Optional[Category]:
    """ViewSet for Category model with nested routing and drf-spectacular documentation.

    Args:
        id (int):
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Category
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        CategoryRequest,
        CategoryRequest,
        CategoryRequest,
    ],
) -> Response[Category]:
    """ViewSet for Category model with nested routing and drf-spectacular documentation.

    Args:
        id (int):
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Category]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        CategoryRequest,
        CategoryRequest,
        CategoryRequest,
    ],
) -> Optional[Category]:
    """ViewSet for Category model with nested routing and drf-spectacular documentation.

    Args:
        id (int):
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.
        body (CategoryRequest): Serializer for Category model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Category
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
