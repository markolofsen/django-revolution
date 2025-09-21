from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_item import OrderItem
from ...types import Response


def _get_kwargs(
    product_id: int,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/private_api/products/{product_id}/order-items/{id}/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[OrderItem]:
    if response.status_code == 200:
        response_200 = OrderItem.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[OrderItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        product_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderItem]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        product_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderItem
    """

    return sync_detailed(
        product_id=product_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        product_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderItem]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        product_id (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderItem
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            id=id,
            client=client,
        )
    ).parsed
