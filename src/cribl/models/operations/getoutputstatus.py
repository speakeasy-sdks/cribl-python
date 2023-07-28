"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import outputstatuses as shared_outputstatuses
from typing import Optional



@dataclasses.dataclass
class GetOutputStatusResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    output_statuses: Optional[shared_outputstatuses.OutputStatuses] = dataclasses.field(default=None)
    r"""a list of OutputStatus objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
