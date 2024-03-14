"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import databaseconnectionconfigs as components_databaseconnectionconfigs
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetListDatabaseConnectionRequest:
    database_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'databaseType', 'style': 'form', 'explode': True }})
    r"""type of database connection"""
    



@dataclasses.dataclass
class GetListDatabaseConnectionResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    database_connection_configs: Optional[components_databaseconnectionconfigs.DatabaseConnectionConfigs] = dataclasses.field(default=None)
    r"""a list of DatabaseConnectionConfig objects"""
    

