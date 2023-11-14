"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import distributedsummaries as components_distributedsummaries
from typing import Optional


@dataclasses.dataclass
class GetDistributedDeploymentRequest:
    mode: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'mode', 'style': 'form', 'explode': True }})
    r"""Filter for worker/group type, either \\"worker\\" for Stream or \\"managed-edge\\" for Edge"""
    



@dataclasses.dataclass
class GetDistributedDeploymentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    distributed_summaries: Optional[components_distributedsummaries.DistributedSummaries] = dataclasses.field(default=None)
    r"""a list of DistributedSummary objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

