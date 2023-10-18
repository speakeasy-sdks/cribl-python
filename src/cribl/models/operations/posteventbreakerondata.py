"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import previewresponses as shared_previewresponses
from typing import Optional


@dataclasses.dataclass
class PostEventBreakerOnDataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    preview_responses: Optional[shared_previewresponses.PreviewResponses] = dataclasses.field(default=None)
    r"""a list of PreviewResponseBody objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

