"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import mappingruleset as components_mappingruleset
from ...models.components import mappingrulesets as components_mappingrulesets
from typing import Optional


@dataclasses.dataclass
class UpdateMappingRulesetsRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    mapping_ruleset: Optional[components_mappingruleset.MappingRuleset] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""MappingRuleset object to be updated"""
    



@dataclasses.dataclass
class UpdateMappingRulesetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    mapping_rulesets: Optional[components_mappingrulesets.MappingRulesets] = dataclasses.field(default=None)
    r"""a list of MappingRuleset objects"""
    

