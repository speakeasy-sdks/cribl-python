"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import kmshealth as components_kmshealth
from typing import Optional


@dataclasses.dataclass
class GetKMSHealthResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    kms_health: Optional[components_kmshealth.KMSHealth] = dataclasses.field(default=None)
    r"""a list of IKMSHealth objects"""
    

