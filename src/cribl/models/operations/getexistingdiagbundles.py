"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import existingdiag as shared_existingdiag
from typing import Optional



@dataclasses.dataclass
class GetExistingDiagBundlesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    existing_diag: Optional[shared_existingdiag.ExistingDiag] = dataclasses.field(default=None)
    r"""a list of Diag objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

