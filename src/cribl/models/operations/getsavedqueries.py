"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import savedqueries as shared_savedqueries
from typing import Optional



@dataclasses.dataclass
class GetSavedQueriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    saved_queries: Optional[shared_savedqueries.SavedQueries] = dataclasses.field(default=None)
    r"""a list of SavedQuery objects"""
    

