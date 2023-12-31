"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import logfilecontents as shared_logfilecontents
from typing import Optional



@dataclasses.dataclass
class GetLogFilesContentsRequest:
    type: str = dataclasses.field(metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    r"""type of logs request single multi group"""
    et: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'et', 'style': 'form', 'explode': True }})
    r"""Epoch timestamp of the earliest event (includes rolled files present on disk)"""
    files: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'files', 'style': 'form', 'explode': True }})
    r"""query string[] optional file or files to query"""
    filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""Filter"""
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'groupId', 'style': 'form', 'explode': True }})
    r"""id of the group to query"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Maximum number of log lines to retrieve starting from offset."""
    lt: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'lt', 'style': 'form', 'explode': True }})
    r"""Epoch timestamp of the latest event (includes rolled files present on disk)"""
    




@dataclasses.dataclass
class GetLogFilesContentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    log_file_contents: Optional[shared_logfilecontents.LogFileContents] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

