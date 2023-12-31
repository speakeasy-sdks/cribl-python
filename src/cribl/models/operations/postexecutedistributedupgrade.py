"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import criblpackage as shared_criblpackage
from ..shared import distributedupgraderequest as shared_distributedupgraderequest
from typing import Optional



@dataclasses.dataclass
class PostExecuteDistributedUpgradeRequest:
    group: str = dataclasses.field(metadata={'path_param': { 'field_name': 'group', 'style': 'simple', 'explode': False }})
    r"""Group to upgrade"""
    distributed_upgrade_request: Optional[shared_distributedupgraderequest.DistributedUpgradeRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""distributedUpgrade object"""
    




@dataclasses.dataclass
class PostExecuteDistributedUpgradeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    cribl_package: Optional[shared_criblpackage.CriblPackage] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

