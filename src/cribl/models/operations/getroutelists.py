"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import routes as shared_routes
from typing import Optional



@dataclasses.dataclass
class GetRouteListsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    routes: Optional[shared_routes.Routes] = dataclasses.field(default=None)
    r"""a list of Routes objects"""
    

