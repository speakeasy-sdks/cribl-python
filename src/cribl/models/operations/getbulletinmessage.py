"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulletinmessage as shared_bulletinmessage
from typing import Optional



@dataclasses.dataclass
class GetBulletinMessageRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetBulletinMessageResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulletin_message: Optional[shared_bulletinmessage.BulletinMessage] = dataclasses.field(default=None)
    r"""a list of BulletinMessage objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

