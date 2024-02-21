"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import jobresult as components_jobresult
from typing import Optional


@dataclasses.dataclass
class GetJobResultRequest:
    group: str = dataclasses.field(metadata={'path_param': { 'field_name': 'group', 'style': 'simple', 'explode': False }})
    r"""Group the job belongs to"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Instance id of the job to get results for"""
    max_files: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'maxFiles', 'style': 'form', 'explode': True }})
    r"""Maximum files to get job results"""
    



@dataclasses.dataclass
class GetJobResultResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    job_result: Optional[components_jobresult.JobResult] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

