"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import loggerconfig as shared_loggerconfig
from typing import Optional


@dataclasses.dataclass
class GetLoggerConfigRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetLoggerConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    logger_config: Optional[shared_loggerconfig.LoggerConfig] = dataclasses.field(default=None)
    r"""a list of LoggerConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

