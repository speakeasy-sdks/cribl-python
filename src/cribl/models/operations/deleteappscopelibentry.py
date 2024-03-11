"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import appscopelibentry as components_appscopelibentry
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class DeleteAppscopeLibEntryRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class DeleteAppscopeLibEntryResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    appscope_lib_entry: Optional[components_appscopelibentry.AppscopeLibEntry] = dataclasses.field(default=None)
    r"""a list of AppscopeLibEntry objects"""
    

