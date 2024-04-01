"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GethSearchJobMetricsRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""search job id"""
    



@dataclasses.dataclass
class GethSearchJobMetricsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    string: Optional[str] = dataclasses.field(default=None)
    r"""string object"""
    

