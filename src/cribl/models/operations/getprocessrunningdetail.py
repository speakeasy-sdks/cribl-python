"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import processes as shared_processes
from typing import Optional



@dataclasses.dataclass
class GetProcessRunningDetailRequest:
    pid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pid', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetProcessRunningDetailResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    processes: Optional[shared_processes.Processes] = dataclasses.field(default=None)
    r"""a list of Process objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

