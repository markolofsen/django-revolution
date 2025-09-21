from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order import Order
from ...models.order_request import OrderRequest
from ...types import Response


def _get_kwargs(
    id: int,
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
        "url": f"/api/private_api/orders/{id}/cancel/",
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
    if response.status_code == 200:
        response_200 = Order.from_dict(response.json())

        return response_200
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Response[Order]:
    """Cancel order

     Cancel an order.

    Args:
        id (int):
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
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Optional[Order]:
    """Cancel order

     Cancel an order.

    Args:
        id (int):
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
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Response[Order]:
    """Cancel order

     Cancel an order.

    Args:
        id (int):
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
        OrderRequest,
        OrderRequest,
        OrderRequest,
    ],
) -> Optional[Order]:
    """Cancel order

     Cancel an order.

    Args:
        id (int):
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
            id=id,
            client=client,
            body=body,
        )
    ).parsed
