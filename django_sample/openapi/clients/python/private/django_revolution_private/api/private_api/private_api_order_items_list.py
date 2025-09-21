from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_order_item_list import PaginatedOrderItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ordering: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ordering"] = ordering

    params["page"] = page

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/private_api/order-items/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedOrderItemList]:
    if response.status_code == 200:
        response_200 = PaginatedOrderItemList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedOrderItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[PaginatedOrderItemList]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        ordering (Union[Unset, str]):
        page (Union[Unset, int]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrderItemList]
    """

    kwargs = _get_kwargs(
        ordering=ordering,
        page=page,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[PaginatedOrderItemList]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        ordering (Union[Unset, str]):
        page (Union[Unset, int]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrderItemList
    """

    return sync_detailed(
        client=client,
        ordering=ordering,
        page=page,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[PaginatedOrderItemList]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        ordering (Union[Unset, str]):
        page (Union[Unset, int]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrderItemList]
    """

    kwargs = _get_kwargs(
        ordering=ordering,
        page=page,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[PaginatedOrderItemList]:
    """ViewSet for OrderItem model with nested routing.

    Args:
        ordering (Union[Unset, str]):
        page (Union[Unset, int]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrderItemList
    """

    return (
        await asyncio_detailed(
            client=client,
            ordering=ordering,
            page=page,
            search=search,
        )
    ).parsed
