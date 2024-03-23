"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import removediagresponse as components_removediagresponse
from typing import Optional


@dataclasses.dataclass
class SendDiagBundleResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    remove_diag_response: Optional[components_removediagresponse.RemoveDiagResponse] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

