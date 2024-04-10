"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import conditions as components_conditions
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetConditionsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    conditions: Optional[components_conditions.Conditions] = dataclasses.field(default=None)
    r"""a list of Condition objects"""
    

