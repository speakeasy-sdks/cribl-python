"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetDiagBundleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_diag_bundle_200_application_tar_plus_gzip_binary_string: Optional[bytes] = dataclasses.field(default=None)
    r"""A tar.gz file consisting all configuration files and recent logs"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

