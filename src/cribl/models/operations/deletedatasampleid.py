"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import datasamples as shared_datasamples
from typing import Optional



@dataclasses.dataclass
class DeleteDataSampleIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class DeleteDataSampleIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    data_samples: Optional[shared_datasamples.DataSamples] = dataclasses.field(default=None)
    r"""a list of DataSample objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
