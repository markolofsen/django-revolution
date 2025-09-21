from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product import Product
from ...types import Response


def _get_kwargs(
    category_id: int,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/private_api/categories/{category_id}/products/{id}/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Product]:
    if response.status_code == 200:
        response_200 = Product.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Product]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        category_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Product]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        category_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Product
    """

    return sync_detailed(
        category_id=category_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    category_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        category_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Product]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        category_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Product
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            id=id,
            client=client,
        )
    ).parsed
