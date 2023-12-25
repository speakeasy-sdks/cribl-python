"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import lookupfile as components_lookupfile
from typing import Optional, Union


@dataclasses.dataclass
class UpdateLookupRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    lookup_file: Optional[Union[components_lookupfile.One, components_lookupfile.Two]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""LookupFile object to be updated"""
    



@dataclasses.dataclass
class UpdateLookupResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    lookup_file: Optional[Union[components_lookupfile.One, components_lookupfile.Two]] = dataclasses.field(default=None)
    r"""a list of LookupFile objects"""
    

