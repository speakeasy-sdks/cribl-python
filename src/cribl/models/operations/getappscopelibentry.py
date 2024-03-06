"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import appscopelibentry as components_appscopelibentry
from typing import Optional


@dataclasses.dataclass
class GetAppscopeLibEntryRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetAppscopeLibEntryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    appscope_lib_entry: Optional[components_appscopelibentry.AppscopeLibEntry] = dataclasses.field(default=None)
    r"""a list of AppscopeLibEntry objects"""
    

