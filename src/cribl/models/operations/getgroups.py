"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import configgroups as shared_configgroups
from typing import Optional



@dataclasses.dataclass
class GetGroupsRequest:
    fields_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""additional fields to add to results: git.commit, git.localChanges, git.log"""
    product: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'product', 'style': 'form', 'explode': True }})
    r"""filter to specific product: \\"stream\\" or \\"edge\\" """
    




@dataclasses.dataclass
class GetGroupsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_groups: Optional[shared_configgroups.ConfigGroups] = dataclasses.field(default=None)
    r"""a list of ConfigGroup objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

