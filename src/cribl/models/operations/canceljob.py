"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import jobcancel as components_jobcancel
from typing import Optional


@dataclasses.dataclass
class CancelJobRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Job instance id"""
    



@dataclasses.dataclass
class CancelJobResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    job_cancel: Optional[components_jobcancel.JobCancel] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

