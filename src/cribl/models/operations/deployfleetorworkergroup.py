"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import configgroup as shared_configgroup
from ..shared import deployrequest as shared_deployrequest
from typing import Optional


@dataclasses.dataclass
class DeployFleetOrWorkerGroupRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    deploy_request: Optional[shared_deployrequest.DeployRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DeployRequest object"""
    



@dataclasses.dataclass
class DeployFleetOrWorkerGroupResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    config_group: Optional[shared_configgroup.ConfigGroup] = dataclasses.field(default=None)
    r"""a list of ConfigGroup objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

