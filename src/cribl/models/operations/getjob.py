"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import jobinfos as components_jobinfos
from typing import Optional


@dataclasses.dataclass
class GetJobRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Job instance id"""
    



@dataclasses.dataclass
class GetJobResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    job_infos: Optional[components_jobinfos.JobInfos] = dataclasses.field(default=None)
    r"""a list of JobInfo objects"""
    

