"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import keymetadataentities as components_keymetadataentities
from ...models.components import keymetadataentity as components_keymetadataentity
from typing import Optional


@dataclasses.dataclass
class UpdateKeyMetadataEntityRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    key_metadata_entity: Optional[components_keymetadataentity.KeyMetadataEntity] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""KeyMetadataEntity object to be updated"""
    



@dataclasses.dataclass
class UpdateKeyMetadataEntityResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    key_metadata_entities: Optional[components_keymetadataentities.KeyMetadataEntities] = dataclasses.field(default=None)
    r"""a list of KeyMetadataEntity objects"""
    

