"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import edgehostfiles as components_edgehostfiles
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetEdgeHostFilesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    edge_host_files: Optional[components_edgehostfiles.EdgeHostFiles] = dataclasses.field(default=None)
    r"""a list of EdgeFileInspectResponse objects"""
    

