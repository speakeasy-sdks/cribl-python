"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import kmshealth as shared_kmshealth
from typing import Optional



@dataclasses.dataclass
class GetKMSHealthResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    kms_health: Optional[shared_kmshealth.KMSHealth] = dataclasses.field(default=None)
    r"""a list of IKMSHealth objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

