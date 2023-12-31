"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchtimeline as shared_searchtimeline
from typing import Optional



@dataclasses.dataclass
class GetSearchTimelineRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""search job id"""
    




@dataclasses.dataclass
class GetSearchTimelineResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    search_timeline: Optional[shared_searchtimeline.SearchTimeline] = dataclasses.field(default=None)
    r"""SearchTimeline object"""
    

