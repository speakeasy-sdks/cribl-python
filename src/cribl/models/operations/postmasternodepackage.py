"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import cribl as components_cribl
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class PostMasterNodePackageResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    cribl: Optional[components_cribl.Cribl] = dataclasses.field(default=None)
    r"""a list of string objects"""
    

