"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import removediagresponse as components_removediagresponse
from typing import Optional


@dataclasses.dataclass
class DeleteDiagBundleRequest:
    path: str = dataclasses.field(metadata={'query_param': { 'field_name': 'path', 'style': 'form', 'explode': True }})
    r"""Diag bundle path"""
    



@dataclasses.dataclass
class DeleteDiagBundleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    remove_diag_response: Optional[components_removediagresponse.RemoveDiagResponse] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

