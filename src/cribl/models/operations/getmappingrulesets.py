"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import mappingrulesets as components_mappingrulesets
from typing import Optional


@dataclasses.dataclass
class GetMappingRulesetsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    mapping_rulesets: Optional[components_mappingrulesets.MappingRulesets] = dataclasses.field(default=None)
    r"""a list of MappingRuleset objects"""
    

