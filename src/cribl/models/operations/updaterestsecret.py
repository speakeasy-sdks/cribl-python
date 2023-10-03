"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import restsecret as shared_restsecret
from typing import Optional



@dataclasses.dataclass
class UpdateRestSecretRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    rest_secret: Optional[shared_restsecret.RestSecret] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""RestSecret object to be updated"""
    




@dataclasses.dataclass
class UpdateRestSecretResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    rest_secret: Optional[shared_restsecret.RestSecret] = dataclasses.field(default=None)
    r"""a list of RestSecret objects"""
    

