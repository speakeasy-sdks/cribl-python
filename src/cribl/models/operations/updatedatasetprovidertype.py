"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import datasetprovidertype as shared_datasetprovidertype
from typing import Optional



@dataclasses.dataclass
class UpdateDatasetProviderTypeRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    dataset_provider_type: Optional[shared_datasetprovidertype.DatasetProviderType] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DatasetProviderType object to be updated"""
    




@dataclasses.dataclass
class UpdateDatasetProviderTypeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dataset_provider_type: Optional[shared_datasetprovidertype.DatasetProviderType] = dataclasses.field(default=None)
    r"""a list of DatasetProviderType objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
