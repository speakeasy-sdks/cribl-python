"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import pipelines as components_pipelines
from typing import Optional


@dataclasses.dataclass
class GetPipelineIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetPipelineIDResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    pipelines: Optional[components_pipelines.Pipelines] = dataclasses.field(default=None)
    r"""a list of Pipeline objects"""
    

