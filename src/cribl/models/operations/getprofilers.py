"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import profileritems as components_profileritems
from typing import Optional


@dataclasses.dataclass
class GetProfilersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    profiler_items: Optional[components_profileritems.ProfilerItems] = dataclasses.field(default=None)
    r"""a list of ProfilerItem objects"""
    

