"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import datasets as shared_datasets
from typing import Optional



@dataclasses.dataclass
class GetDatasetObjectsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    datasets: Optional[shared_datasets.Datasets] = dataclasses.field(default=None)
    r"""a list of Dataset objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

