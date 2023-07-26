"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import jobdelete as shared_jobdelete
from typing import Optional



@dataclasses.dataclass
class DeleteJobRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Job instance id"""
    




@dataclasses.dataclass
class DeleteJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    job_delete: Optional[shared_jobdelete.JobDelete] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

