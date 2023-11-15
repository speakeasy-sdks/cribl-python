"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import outputtestrequest as components_outputtestrequest
from ...models.components import outputtestresponses as components_outputtestresponses
from typing import Optional


@dataclasses.dataclass
class PostSampleOutputRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Output Id"""
    output_test_request: Optional[components_outputtestrequest.OutputTestRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""OutputTestRequest object"""
    



@dataclasses.dataclass
class PostSampleOutputResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    output_test_responses: Optional[components_outputtestresponses.OutputTestResponses] = dataclasses.field(default=None)
    r"""a list of OutputTestResponse objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

