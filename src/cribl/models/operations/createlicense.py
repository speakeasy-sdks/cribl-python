"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import license as components_license
from typing import Optional


@dataclasses.dataclass
class CreateLicenseResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    license: Optional[components_license.License] = dataclasses.field(default=None)
    r"""a list of License objects"""
    

