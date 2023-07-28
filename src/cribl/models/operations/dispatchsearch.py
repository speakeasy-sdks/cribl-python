"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchid as shared_searchid
from typing import Optional



@dataclasses.dataclass
class DispatchSearchRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""search job id"""
    




@dataclasses.dataclass
class DispatchSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    search_id: Optional[shared_searchid.SearchID] = dataclasses.field(default=None)
    r"""a list of any objects"""
    
