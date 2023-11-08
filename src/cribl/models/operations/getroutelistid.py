"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import routes as components_routes
from typing import Optional


@dataclasses.dataclass
class GetRouteListIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""There is only one route entity and it should be accessed with id: default."""
    



@dataclasses.dataclass
class GetRouteListIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    routes: Optional[components_routes.Routes] = dataclasses.field(default=None)
    r"""a list of Routes objects"""
    

