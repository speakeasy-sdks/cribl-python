"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gitsettings as shared_gitsettings
from typing import Optional



@dataclasses.dataclass
class UpdateGitSettingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    git_settings: Optional[shared_gitsettings.GitSettings] = dataclasses.field(default=None)
    r"""a list of GitSettings objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

