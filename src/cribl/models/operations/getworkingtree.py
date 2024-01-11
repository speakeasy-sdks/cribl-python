"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import gitstatusresults as components_gitstatusresults
from typing import Optional


@dataclasses.dataclass
class GetWorkingTreeRequest:
    group: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'group', 'style': 'form', 'explode': True }})
    r"""Group ID"""
    



@dataclasses.dataclass
class GetWorkingTreeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    git_status_results: Optional[components_gitstatusresults.GitStatusResults] = dataclasses.field(default=None)
    r"""a list of GitStatusResult objects"""
    

