"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import eventbreakerrulesets as shared_eventbreakerrulesets
from typing import Optional



@dataclasses.dataclass
class GetEventBreakerIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetEventBreakerIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    event_breaker_rulesets: Optional[shared_eventbreakerrulesets.EventBreakerRulesets] = dataclasses.field(default=None)
    r"""a list of Event Breaker Ruleset objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

