"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import lookupfileinforesponse as shared_lookupfileinforesponse
from typing import Optional



@dataclasses.dataclass
class UploadLookupRequest:
    filename: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filename', 'style': 'form', 'explode': True }})
    r"""query LookupFilenameSchema required Filename"""
    




@dataclasses.dataclass
class UploadLookupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    lookup_file_info_response: Optional[shared_lookupfileinforesponse.LookupFileInfoResponse] = dataclasses.field(default=None)
    r"""LookupFileInfoResponse object"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
