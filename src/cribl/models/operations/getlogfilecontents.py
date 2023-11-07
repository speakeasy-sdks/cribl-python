"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import logfilecontents as components_logfilecontents
from typing import Optional


@dataclasses.dataclass
class GetLogFileContentsRequest:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    r"""Group ID (optional)"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Job id"""
    end_offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'endOffset', 'style': 'form', 'explode': True }})
    r"""in the current log file to fetch the log events upto."""
    et: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'et', 'style': 'form', 'explode': True }})
    r"""Epoch timestamp of the earliest event (includes rolled files present on disk)"""
    filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""Filter"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Maximum number of log lines to retrieve starting from offset."""
    lt: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'lt', 'style': 'form', 'explode': True }})
    r"""Epoch timestamp of the latest event (includes rolled files present on disk)"""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Offset in the current log file to fetch the log events from."""
    



@dataclasses.dataclass
class GetLogFileContentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    log_file_contents: Optional[components_logfilecontents.LogFileContents] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

