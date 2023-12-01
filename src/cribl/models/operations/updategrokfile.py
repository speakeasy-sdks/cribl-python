"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import grokfile as components_grokfile
from typing import Optional


@dataclasses.dataclass
class UpdateGrokFileRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    grok_file: Optional[components_grokfile.GrokFile] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""GrokFile object to be updated"""
    



@dataclasses.dataclass
class UpdateGrokFileResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    grok_file: Optional[components_grokfile.GrokFile] = dataclasses.field(default=None)
    r"""a list of GrokFile objects"""
    

