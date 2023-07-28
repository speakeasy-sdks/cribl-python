"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appscopelibentries as shared_appscopelibentries
from typing import Optional



@dataclasses.dataclass
class GetAppscopeLibEntriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    app_scope_lib_entries: Optional[shared_appscopelibentries.AppScopeLibEntries] = dataclasses.field(default=None)
    r"""a list of AppscopeLibEntry objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
