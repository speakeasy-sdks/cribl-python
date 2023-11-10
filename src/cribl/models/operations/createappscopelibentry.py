"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import appscopelibentry as components_appscopelibentry
from typing import Optional


@dataclasses.dataclass
class CreateAppscopeLibEntryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    appscope_lib_entry: Optional[components_appscopelibentry.AppscopeLibEntry] = dataclasses.field(default=None)
    r"""a list of AppscopeLibEntry objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

