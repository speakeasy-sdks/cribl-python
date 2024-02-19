"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import lookupfiles as components_lookupfiles
from typing import Optional


@dataclasses.dataclass
class CreateLookupResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    lookup_files: Optional[components_lookupfiles.LookupFiles] = dataclasses.field(default=None)
    r"""a list of LookupFile objects"""
    

