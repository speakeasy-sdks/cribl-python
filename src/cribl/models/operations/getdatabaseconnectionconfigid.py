"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import databaseconnectionconfigs as components_databaseconnectionconfigs
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetDatabaseConnectionConfigIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetDatabaseConnectionConfigIDResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    database_connection_configs: Optional[components_databaseconnectionconfigs.DatabaseConnectionConfigs] = dataclasses.field(default=None)
    r"""a list of DatabaseConnectionConfig objects"""
    

