"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import parserlibentries as components_parserlibentries
from typing import Optional


@dataclasses.dataclass
class PostParserObjectResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    parser_lib_entries: Optional[components_parserlibentries.ParserLibEntries] = dataclasses.field(default=None)
    r"""a list of Parser objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

