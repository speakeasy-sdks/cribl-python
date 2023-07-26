"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import savedquery as shared_savedquery
from typing import Optional



@dataclasses.dataclass
class DeleteSavedQueriesRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class DeleteSavedQueriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    saved_query: Optional[shared_savedquery.SavedQuery] = dataclasses.field(default=None)
    r"""a list of SavedQuery objects"""
    

