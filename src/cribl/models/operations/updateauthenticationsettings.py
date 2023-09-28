"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import authconfigs as shared_authconfigs
from typing import Optional



@dataclasses.dataclass
class UpdateAuthenticationSettingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    auth_configs: Optional[shared_authconfigs.AuthConfigs] = dataclasses.field(default=None)
    r"""a list of AuthConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

