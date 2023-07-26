"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cribl as shared_cribl
from typing import Optional



@dataclasses.dataclass
class PostMasterNodePackageResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    cribl: Optional[shared_cribl.Cribl] = dataclasses.field(default=None)
    r"""a list of string objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

