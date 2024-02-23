"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import success as errors_success
from typing import Optional


@dataclasses.dataclass
class PostRequestAuthRequestBody:
    r"""Authentication request object"""
    relay_state: Optional[str] = dataclasses.field(default=None, metadata={'form': { 'field_name': 'RelayState' }})
    saml_response: Optional[str] = dataclasses.field(default=None, metadata={'form': { 'field_name': 'SAMLResponse' }})
    r"""Authentication request object"""
    



@dataclasses.dataclass
class PostRequestAuthResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    success: Optional[errors_success.Success] = dataclasses.field(default=None)
    r"""Authentication success"""
    

