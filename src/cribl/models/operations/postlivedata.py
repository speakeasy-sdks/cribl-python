"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import livedata as components_livedata
from typing import Optional


@dataclasses.dataclass
class PostLiveDataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    live_data: Optional[components_livedata.LiveData] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

