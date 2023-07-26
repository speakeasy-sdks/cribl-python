"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import keymetadataentities as shared_keymetadataentities
from ..shared import keymetadataentity as shared_keymetadataentity
from typing import Optional



@dataclasses.dataclass
class UpdateKeyMetadataEntityRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    key_metadata_entity: Optional[shared_keymetadataentity.KeyMetadataEntity] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""KeyMetadataEntity object to be updated"""
    




@dataclasses.dataclass
class UpdateKeyMetadataEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    key_metadata_entities: Optional[shared_keymetadataentities.KeyMetadataEntities] = dataclasses.field(default=None)
    r"""a list of KeyMetadataEntity objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

