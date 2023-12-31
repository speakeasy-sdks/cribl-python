"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import authpolicyentries as shared_authpolicyentries
from typing import Optional



@dataclasses.dataclass
class GetAuthorizationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    auth_policy_entries: Optional[shared_authpolicyentries.AuthPolicyEntries] = dataclasses.field(default=None)
    r"""a list of AuthPolicyEntry objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

