"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import regexlibentries as shared_regexlibentries
from typing import Optional



@dataclasses.dataclass
class PostRegexLibEntryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    regex_lib_entries: Optional[shared_regexlibentries.RegexLibEntries] = dataclasses.field(default=None)
    r"""a list of RegexLibEntry objects"""
    

