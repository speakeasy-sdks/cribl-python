"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import pipelines as shared_pipelines
from typing import Optional



@dataclasses.dataclass
class PostCreatePipelineResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    pipelines: Optional[shared_pipelines.Pipelines] = dataclasses.field(default=None)
    r"""a list of Pipeline objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

