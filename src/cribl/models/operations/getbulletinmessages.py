"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulletinmessages as shared_bulletinmessages
from typing import Optional



@dataclasses.dataclass
class GetBulletinMessagesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulletin_messages: Optional[shared_bulletinmessages.BulletinMessages] = dataclasses.field(default=None)
    r"""a list of BulletinMessage objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
