"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import eventbreakerrulesets as components_eventbreakerrulesets
from typing import Optional


@dataclasses.dataclass
class GetEventBreakerIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclasses.dataclass
class GetEventBreakerIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    event_breaker_rulesets: Optional[components_eventbreakerrulesets.EventBreakerRulesets] = dataclasses.field(default=None)
    r"""a list of Event Breaker Ruleset objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

