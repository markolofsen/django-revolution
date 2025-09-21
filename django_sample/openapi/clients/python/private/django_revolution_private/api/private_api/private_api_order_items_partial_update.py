from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_item import OrderItem
from ...models.patched_order_item_request import PatchedOrderItemRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/private_api/order-items/{id}/",
    }

    if isinstance(body, PatchedOrderItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedOrderItemRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedOrderItemRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
    ],
) -> Response[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        id (int):
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderItem]
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
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
    ],
) -> Optional[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        id (int):
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderItem
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
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
    ],
) -> Response[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        id (int):
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderItem]
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
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
        PatchedOrderItemRequest,
    ],
) -> Optional[OrderItem]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        id (int):
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.
        body (PatchedOrderItemRequest): Serializer for OrderItem model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderItem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
