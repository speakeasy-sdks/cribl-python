"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import schemalibentry as components_schemalibentry
from typing import Optional


@dataclasses.dataclass
class UpdateSchemaRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    schema_lib_entry: Optional[components_schemalibentry.SchemaLibEntry] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Schema object to be updated"""
    



@dataclasses.dataclass
class UpdateSchemaResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    schema_lib_entry: Optional[components_schemalibentry.SchemaLibEntry] = dataclasses.field(default=None)
    r"""a list of Schema objects"""
    

