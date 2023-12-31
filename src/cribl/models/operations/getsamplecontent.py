"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import samplecontents as shared_samplecontents
from typing import Optional



@dataclasses.dataclass
class GetSampleContentRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Sample ID"""
    




@dataclasses.dataclass
class GetSampleContentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    sample_contents: Optional[shared_samplecontents.SampleContents] = dataclasses.field(default=None)
    r"""a list of SampleContent objects"""
    

