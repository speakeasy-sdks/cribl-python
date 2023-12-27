"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import pipeline as components_pipeline
from ...models.components import pipelines as components_pipelines
from typing import Optional


@dataclasses.dataclass
class UpdatePipelineIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    pipeline: Optional[components_pipeline.Pipeline] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Pipeline object to be updated"""
    



@dataclasses.dataclass
class UpdatePipelineIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    pipelines: Optional[components_pipelines.Pipelines] = dataclasses.field(default=None)
    r"""a list of Pipeline objects"""
    

