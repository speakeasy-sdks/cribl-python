"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import featuresentries as shared_featuresentries
from typing import Optional



@dataclasses.dataclass
class GetFeaturesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    features_entries: Optional[shared_featuresentries.FeaturesEntries] = dataclasses.field(default=None)
    r"""a list of FeaturesEntry objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

