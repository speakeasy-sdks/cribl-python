"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cancelrunninggroup as shared_cancelrunninggroup
from typing import Optional



@dataclasses.dataclass
class PostCancelRunningGroupRequest:
    group: str = dataclasses.field(metadata={'path_param': { 'field_name': 'group', 'style': 'simple', 'explode': False }})
    r"""id of the group"""
    




@dataclasses.dataclass
class PostCancelRunningGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    cancel_running_group: Optional[shared_cancelrunninggroup.CancelRunningGroup] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

