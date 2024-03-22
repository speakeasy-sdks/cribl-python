"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import gitsettings as components_gitsettings
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class UpdateCriblsSettingsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    git_settings: Optional[components_gitsettings.GitSettings] = dataclasses.field(default=None)
    r"""a list of string objects"""
    

