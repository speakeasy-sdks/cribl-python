"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import jobinfos as shared_jobinfos
from typing import Optional



@dataclasses.dataclass
class PreventJobRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Job Instance id"""
    




@dataclasses.dataclass
class PreventJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    job_infos: Optional[shared_jobinfos.JobInfos] = dataclasses.field(default=None)
    r"""a list of JobInfo objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

