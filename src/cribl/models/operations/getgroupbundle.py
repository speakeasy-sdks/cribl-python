"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import deployrequest as components_deployrequest
from ...models.components import groupbundle as components_groupbundle
from typing import Optional


@dataclasses.dataclass
class GetGroupBundleRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Group ID"""
    deploy_request: Optional[components_deployrequest.DeployRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DeployRequest object"""
    



@dataclasses.dataclass
class GetGroupBundleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    group_bundle: Optional[components_groupbundle.GroupBundle] = dataclasses.field(default=None)
    r"""a list of string objects"""
    

