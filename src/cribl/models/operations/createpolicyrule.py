"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import policyrules as shared_policyrules
from typing import Optional



@dataclasses.dataclass
class CreatePolicyRuleResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    policy_rules: Optional[shared_policyrules.PolicyRules] = dataclasses.field(default=None)
    r"""a list of PolicyRule objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

