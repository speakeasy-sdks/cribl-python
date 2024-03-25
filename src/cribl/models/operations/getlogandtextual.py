"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import textualdiff as components_textualdiff
from typing import Optional


@dataclasses.dataclass
class GetLogandTextualRequest:
    commit: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'commit', 'style': 'form', 'explode': True }})
    r"""Commit hash (default is HEAD)"""
    group: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'group', 'style': 'form', 'explode': True }})
    r"""Group ID"""
    



@dataclasses.dataclass
class GetLogandTextualResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    textual_diff: Optional[components_textualdiff.TextualDiff] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

