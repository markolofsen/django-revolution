from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_product_request import PatchedProductRequest
from ...models.product import Product
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedProductRequest,
        PatchedProductRequest,
        PatchedProductRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/private_api/products/{id}/",
    }

    if isinstance(body, PatchedProductRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedProductRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedProductRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedProductRequest,
        PatchedProductRequest,
        PatchedProductRequest,
    ],
) -> Response[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        id (int):
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Product]
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
        PatchedProductRequest,
        PatchedProductRequest,
        PatchedProductRequest,
    ],
) -> Optional[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        id (int):
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Product
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
        PatchedProductRequest,
        PatchedProductRequest,
        PatchedProductRequest,
    ],
) -> Response[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        id (int):
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Product]
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
        PatchedProductRequest,
        PatchedProductRequest,
        PatchedProductRequest,
    ],
) -> Optional[Product]:
    """ViewSet for Product model with nested routing.

    Args:
        id (int):
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.
        body (PatchedProductRequest): Serializer for Product model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Product
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
