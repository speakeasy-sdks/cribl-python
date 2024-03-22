"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import eventbreakerruleset as components_eventbreakerruleset
from ...models.components import eventbreakerrulesets as components_eventbreakerrulesets
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class UpdateEventBreakerRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    event_breaker_ruleset: Optional[components_eventbreakerruleset.EventBreakerRuleset] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Event Breaker Ruleset object to be updated"""
    



@dataclasses.dataclass
class UpdateEventBreakerResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    event_breaker_rulesets: Optional[components_eventbreakerrulesets.EventBreakerRulesets] = dataclasses.field(default=None)
    r"""a list of Event Breaker Ruleset objects"""
    

