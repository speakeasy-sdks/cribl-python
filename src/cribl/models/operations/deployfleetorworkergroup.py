"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import configgroup as components_configgroup
from ...models.components import deployrequest as components_deployrequest
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class DeployFleetOrWorkerGroupRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    deploy_request: Optional[components_deployrequest.DeployRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DeployRequest object"""
    



@dataclasses.dataclass
class DeployFleetOrWorkerGroupResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    config_group: Optional[components_configgroup.ConfigGroup] = dataclasses.field(default=None)
    r"""a list of ConfigGroup objects"""
    

