"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import featuresentries as components_featuresentries
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetFeaturesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    features_entries: Optional[components_featuresentries.FeaturesEntries] = dataclasses.field(default=None)
    r"""a list of FeaturesEntry objects"""
    

