"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taskerrors as shared_taskerrors
from typing import Optional


@dataclasses.dataclass
class GetTaskErrorsRequest:
    group: str = dataclasses.field(metadata={'path_param': { 'field_name': 'group', 'style': 'simple', 'explode': False }})
    r"""Group the job belongs to"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Instance id of the job to get results for"""
    



@dataclasses.dataclass
class GetTaskErrorsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_errors: Optional[shared_taskerrors.TaskErrors] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

