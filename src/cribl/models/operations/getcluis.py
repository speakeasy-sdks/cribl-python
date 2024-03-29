"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import cluiitems as components_cluiitems
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetCluisRequest:
    query: str = dataclasses.field(metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Search query"""
    context: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'context', 'style': 'form', 'explode': True }})
    r"""Search query context, either \\"stream\\" or \\"edge\\" """
    



@dataclasses.dataclass
class GetCluisResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    clui_items: Optional[components_cluiitems.CluiItems] = dataclasses.field(default=None)
    r"""a list of CluiItem objects"""
    

