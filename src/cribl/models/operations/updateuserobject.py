"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import user as shared_user
from ..shared import users as shared_users
from typing import Optional



@dataclasses.dataclass
class UpdateUserObjectRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    user: Optional[shared_user.User] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""User object"""
    




@dataclasses.dataclass
class UpdateUserObjectResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    users: Optional[shared_users.Users] = dataclasses.field(default=None)
    r"""a list of User objects"""
    

