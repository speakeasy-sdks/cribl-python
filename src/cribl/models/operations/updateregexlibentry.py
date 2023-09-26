"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import regexlibentries as shared_regexlibentries
from ..shared import regexlibentry as shared_regexlibentry
from typing import Optional



@dataclasses.dataclass
class UpdateRegexLibEntryRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    regex_lib_entry: Optional[shared_regexlibentry.RegexLibEntry] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""RegexLibEntry object to be updated"""
    




@dataclasses.dataclass
class UpdateRegexLibEntryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    regex_lib_entries: Optional[shared_regexlibentries.RegexLibEntries] = dataclasses.field(default=None)
    r"""a list of RegexLibEntry objects"""
    

