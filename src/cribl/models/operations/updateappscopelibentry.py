"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appscopelibentry as shared_appscopelibentry
from typing import Optional



@dataclasses.dataclass
class UpdateAppscopeLibEntryRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    appscope_lib_entry: Optional[shared_appscopelibentry.AppscopeLibEntry] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""AppscopeLibEntry object to be updated"""
    




@dataclasses.dataclass
class UpdateAppscopeLibEntryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    appscope_lib_entry: Optional[shared_appscopelibentry.AppscopeLibEntry] = dataclasses.field(default=None)
    r"""a list of AppscopeLibEntry objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

