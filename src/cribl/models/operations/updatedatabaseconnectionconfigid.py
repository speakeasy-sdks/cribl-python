"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import databaseconnectionconfig as shared_databaseconnectionconfig
from ..shared import databaseconnectionconfigs as shared_databaseconnectionconfigs
from typing import Optional



@dataclasses.dataclass
class UpdateDatabaseConnectionConfigIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    database_connection_config: Optional[shared_databaseconnectionconfig.DatabaseConnectionConfig] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DatabaseConnectionConfig object to be updated"""
    




@dataclasses.dataclass
class UpdateDatabaseConnectionConfigIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    database_connection_configs: Optional[shared_databaseconnectionconfigs.DatabaseConnectionConfigs] = dataclasses.field(default=None)
    r"""a list of DatabaseConnectionConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

