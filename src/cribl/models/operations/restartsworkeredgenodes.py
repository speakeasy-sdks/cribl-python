"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import restartresponses as components_restartresponses
from typing import Optional


@dataclasses.dataclass
class RestartsWorkerEdgeNodesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    restart_responses: Optional[components_restartresponses.RestartResponses] = dataclasses.field(default=None)
    r"""a list of RestartResponse objects"""
    

