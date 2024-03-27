"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import searchid as components_searchid
from typing import Optional


@dataclasses.dataclass
class DispatchSearchRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""search job id"""
    



@dataclasses.dataclass
class DispatchSearchResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    search_id: Optional[components_searchid.SearchID] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

