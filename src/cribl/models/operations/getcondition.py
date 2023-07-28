"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import conditions as shared_conditions
from typing import Optional



@dataclasses.dataclass
class GetConditionRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetConditionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    conditions: Optional[shared_conditions.Conditions] = dataclasses.field(default=None)
    r"""a list of Condition objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
