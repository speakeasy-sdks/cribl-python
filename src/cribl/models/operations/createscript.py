"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import scriptlibentry as components_scriptlibentry
from typing import Optional


@dataclasses.dataclass
class CreateScriptResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    script_lib_entry: Optional[components_scriptlibentry.ScriptLibEntry] = dataclasses.field(default=None)
    r"""a list of Script objects"""
    

