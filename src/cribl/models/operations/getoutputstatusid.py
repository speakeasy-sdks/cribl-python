"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import outputstatuses as components_outputstatuses
from typing import Optional


@dataclasses.dataclass
class GetOutputStatusIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetOutputStatusIDResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    output_statuses: Optional[components_outputstatuses.OutputStatuses] = dataclasses.field(default=None)
    r"""a list of OutputStatus objects"""
    

