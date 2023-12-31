"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import databaseconnectionconfigs as shared_databaseconnectionconfigs
from typing import Optional



@dataclasses.dataclass
class GetDatabaseConnectionConfigIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetDatabaseConnectionConfigIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    database_connection_configs: Optional[shared_databaseconnectionconfigs.DatabaseConnectionConfigs] = dataclasses.field(default=None)
    r"""a list of DatabaseConnectionConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

