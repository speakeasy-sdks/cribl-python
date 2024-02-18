"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import featuresentries as components_featuresentries
from typing import Optional


@dataclasses.dataclass
class GetFeaturesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    features_entries: Optional[components_featuresentries.FeaturesEntries] = dataclasses.field(default=None)
    r"""a list of FeaturesEntry objects"""
    

