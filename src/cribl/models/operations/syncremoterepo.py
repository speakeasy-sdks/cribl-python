"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gitstatusresults as shared_gitstatusresults
from typing import Optional



@dataclasses.dataclass
class SyncRemoteRepoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    git_status_results: Optional[shared_gitstatusresults.GitStatusResults] = dataclasses.field(default=None)
    r"""a list of GitStatusResult objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
