"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import user as components_user
from ...models.components import users as components_users
from typing import Optional


@dataclasses.dataclass
class UpdateUserObjectRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    user: Optional[components_user.User] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""User object"""
    



@dataclasses.dataclass
class UpdateUserObjectResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    users: Optional[components_users.Users] = dataclasses.field(default=None)
    r"""a list of User objects"""
    

