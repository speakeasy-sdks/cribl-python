"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import certificate as shared_certificate
from typing import Optional


@dataclasses.dataclass
class UpdateCertificateRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    certificate: Optional[shared_certificate.Certificate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Certificate object to be updated"""
    



@dataclasses.dataclass
class UpdateCertificateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    certificate: Optional[shared_certificate.Certificate] = dataclasses.field(default=None)
    r"""a list of Certificate objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

