"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import packinfos as components_packinfos
from typing import Optional


@dataclasses.dataclass
class UninstallPackRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Pack name"""
    



@dataclasses.dataclass
class UninstallPackResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    pack_infos: Optional[components_packinfos.PackInfos] = dataclasses.field(default=None)
    r"""a list of PackInfo objects"""
    

