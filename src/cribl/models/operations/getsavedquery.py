"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import savedquery as components_savedquery
from typing import Optional


@dataclasses.dataclass
class GetSavedQueryRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetSavedQueryResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    saved_query: Optional[components_savedquery.SavedQuery] = dataclasses.field(default=None)
    r"""a list of SavedQuery objects"""
    

