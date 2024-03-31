"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import crudentitybases as components_crudentitybases
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetListAuthGroupResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    crud_entity_bases: Optional[components_crudentitybases.CrudEntityBases] = dataclasses.field(default=None)
    r"""a list of CrudEntityBase objects"""
    

