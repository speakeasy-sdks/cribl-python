"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import logfilesinfo as shared_logfilesinfo
from typing import Optional



@dataclasses.dataclass
class GetLogFilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    log_files_info: Optional[shared_logfilesinfo.LogFilesInfo] = dataclasses.field(default=None)
    r"""a list of LogFileInfo objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

