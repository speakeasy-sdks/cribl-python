"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import logfilecontents as components_logfilecontents
from typing import Optional


@dataclasses.dataclass
class GetLogFileContentRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Log ID"""
    end_offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'endOffset', 'style': 'form', 'explode': True }})
    r"""in the current log file to fetch the log events upto."""
    et: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'et', 'style': 'form', 'explode': True }})
    r"""Epoch timestamp of the earliest event (includes rolled files present on disk)"""
    filter_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""Filter"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Maximum number of log lines to retrieve starting from offset."""
    lt: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'lt', 'style': 'form', 'explode': True }})
    r"""Epoch timestamp of the latest event (includes rolled files present on disk)"""
    



@dataclasses.dataclass
class GetLogFileContentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    log_file_contents: Optional[components_logfilecontents.LogFileContents] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

