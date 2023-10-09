"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cribl as shared_cribl
from typing import Optional



@dataclasses.dataclass
class PostGiveCriblVersionRequest:
    version: str = dataclasses.field(metadata={'path_param': { 'field_name': 'version', 'style': 'simple', 'explode': False }})
    r"""Version number"""
    




@dataclasses.dataclass
class PostGiveCriblVersionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    cribl: Optional[shared_cribl.Cribl] = dataclasses.field(default=None)
    r"""a list of string objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

