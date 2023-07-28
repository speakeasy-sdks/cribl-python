"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetDiagBundlesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_diag_bundles_200_application_tar_plus_gzip_binary_string: Optional[bytes] = dataclasses.field(default=None)
    r"""Get list of existing diag bundles"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
