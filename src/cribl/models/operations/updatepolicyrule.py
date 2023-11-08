"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import policyrule as components_policyrule
from ...models.components import policyrules as components_policyrules
from typing import Optional


@dataclasses.dataclass
class UpdatePolicyRuleRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    policy_rule: Optional[components_policyrule.PolicyRule] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""PolicyRule object to be updated"""
    



@dataclasses.dataclass
class UpdatePolicyRuleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    policy_rules: Optional[components_policyrules.PolicyRules] = dataclasses.field(default=None)
    r"""a list of PolicyRule objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

