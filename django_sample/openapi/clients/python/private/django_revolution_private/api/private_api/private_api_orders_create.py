from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order import Order
from ...models.order_request import OrderRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/private_api/orders/",
    }

    if isinstance(body, OrderRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, OrderRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OrderRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Order]:
    if response.status_code == 201:
        response_201 = Order.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Order]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Response[Order]:
    """ViewSet for Order model with nested routing.

    Args:
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Optional[Order]:
    """ViewSet for Order model with nested routing.

    Args:
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Response[Order]:
    """ViewSet for Order model with nested routing.

    Args:
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Optional[Order]:
    """ViewSet for Order model with nested routing.

    Args:
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.
        body (OrderRequest): Serializer for Order model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
