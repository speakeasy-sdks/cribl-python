"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import jobresume as shared_jobresume
from typing import Optional



@dataclasses.dataclass
class ResumeJobRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Job instance id"""
    




@dataclasses.dataclass
class ResumeJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    job_resume: Optional[shared_jobresume.JobResume] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

