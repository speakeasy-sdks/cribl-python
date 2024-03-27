"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import grokfiles as components_grokfiles
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetGrokFilesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    grok_files: Optional[components_grokfiles.GrokFiles] = dataclasses.field(default=None)
    r"""a list of GrokFile objects"""
    

