"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import pushconfig as components_pushconfig
from typing import Optional


@dataclasses.dataclass
class PushCurrentConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    push_config: Optional[components_pushconfig.PushConfig] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

