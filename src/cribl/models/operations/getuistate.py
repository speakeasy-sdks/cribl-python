"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import uistates as shared_uistates
from typing import Optional



@dataclasses.dataclass
class GetUIStateRequest:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    r"""UI state key"""
    




@dataclasses.dataclass
class GetUIStateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    ui_states: Optional[shared_uistates.UIStates] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

