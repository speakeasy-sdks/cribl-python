"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import scriptlibentries as shared_scriptlibentries
from typing import Optional



@dataclasses.dataclass
class GetScriptsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    script_lib_entries: Optional[shared_scriptlibentries.ScriptLibEntries] = dataclasses.field(default=None)
    r"""a list of Script objects"""
    

