"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import loggerconfig as components_loggerconfig
from typing import Optional


@dataclasses.dataclass
class UpdateLoggerConfigRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    logger_config: Optional[components_loggerconfig.LoggerConfig] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""LoggerConfig object to be updated"""
    



@dataclasses.dataclass
class UpdateLoggerConfigResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    logger_config: Optional[components_loggerconfig.LoggerConfig] = dataclasses.field(default=None)
    r"""a list of LoggerConfig objects"""
    

