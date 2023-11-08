"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import grokfiles as components_grokfiles
from typing import Optional


@dataclasses.dataclass
class GetGrokFilesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    grok_files: Optional[components_grokfiles.GrokFiles] = dataclasses.field(default=None)
    r"""a list of GrokFile objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

