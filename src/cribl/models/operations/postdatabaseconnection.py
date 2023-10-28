"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import databaseconnectionconfigs as shared_databaseconnectionconfigs
from typing import Optional


@dataclasses.dataclass
class PostDatabaseConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    database_connection_configs: Optional[shared_databaseconnectionconfigs.DatabaseConnectionConfigs] = dataclasses.field(default=None)
    r"""a list of DatabaseConnectionConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

