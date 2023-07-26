"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import restsecret as shared_restsecret
from typing import Optional



@dataclasses.dataclass
class DeleteRestSecretRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class DeleteRestSecretResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    rest_secret: Optional[shared_restsecret.RestSecret] = dataclasses.field(default=None)
    r"""a list of RestSecret objects"""
    

