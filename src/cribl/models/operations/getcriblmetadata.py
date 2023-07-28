"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetCriblMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_cribl_metadata_200_text_xml_string: Optional[str] = dataclasses.field(default=None)
    r"""Service Provider metadata"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
