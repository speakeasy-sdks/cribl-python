"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import mappingrulesets as shared_mappingrulesets
from typing import Optional



@dataclasses.dataclass
class GetMappingRulesetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetMappingRulesetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    mapping_rulesets: Optional[shared_mappingrulesets.MappingRulesets] = dataclasses.field(default=None)
    r"""a list of MappingRuleset objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

