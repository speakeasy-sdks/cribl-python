"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import keymetadataentities as components_keymetadataentities
from typing import Optional


@dataclasses.dataclass
class CreateKeyMetadataEntityResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    key_metadata_entities: Optional[components_keymetadataentities.KeyMetadataEntities] = dataclasses.field(default=None)
    r"""a list of KeyMetadataEntity objects"""
    

