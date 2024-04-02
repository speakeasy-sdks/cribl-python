"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import gitsettingsresponse as components_gitsettingsresponse
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetGitSettingsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    git_settings_response: Optional[components_gitsettingsresponse.GitSettingsResponse] = dataclasses.field(default=None)
    r"""a list of GitSettings objects"""
    

