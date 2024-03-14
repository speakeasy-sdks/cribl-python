"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import loggerconfig as components_loggerconfig
from typing import Optional


@dataclasses.dataclass
class DeleteLoggerConfigRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class DeleteLoggerConfigResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    logger_config: Optional[components_loggerconfig.LoggerConfig] = dataclasses.field(default=None)
    r"""a list of LoggerConfig objects"""
    

