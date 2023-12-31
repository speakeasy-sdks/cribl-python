"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import edgefiles as shared_edgefiles
from typing import Optional



@dataclasses.dataclass
class GetLogFileListRequest:
    allow: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'allow', 'style': 'form', 'explode': True }})
    r"""query array[string] optional List of allowed-filename wildcard patterns"""
    depth: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'depth', 'style': 'form', 'explode': True }})
    r"""Search depth for \\"manual\\" mode"""
    mode: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'mode', 'style': 'form', 'explode': True }})
    r"""Discovery Mode (default is \\"auto\\")"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'path', 'style': 'form', 'explode': True }})
    r"""Search directory for \\"manual\\" mode"""
    




@dataclasses.dataclass
class GetLogFileListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    edge_files: Optional[shared_edgefiles.EdgeFiles] = dataclasses.field(default=None)
    r"""a list of EdgeFile objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

