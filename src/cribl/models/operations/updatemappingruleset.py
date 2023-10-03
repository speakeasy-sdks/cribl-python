"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import mappingruleset as shared_mappingruleset
from ..shared import mappingrulesets as shared_mappingrulesets
from typing import Optional



@dataclasses.dataclass
class UpdateMappingRulesetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    mapping_ruleset: Optional[shared_mappingruleset.MappingRuleset] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""MappingRuleset object to be updated"""
    




@dataclasses.dataclass
class UpdateMappingRulesetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    mapping_rulesets: Optional[shared_mappingrulesets.MappingRulesets] = dataclasses.field(default=None)
    r"""a list of MappingRuleset objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

