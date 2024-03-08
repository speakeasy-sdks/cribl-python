"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import certificate as components_certificate
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class UpdateCertificateRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    certificate: Optional[components_certificate.Certificate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Certificate object to be updated"""
    



@dataclasses.dataclass
class UpdateCertificateResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    certificate: Optional[components_certificate.Certificate] = dataclasses.field(default=None)
    r"""a list of Certificate objects"""
    

