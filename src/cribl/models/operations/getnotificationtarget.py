"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import notificationtargets as shared_notificationtargets
from typing import Optional



@dataclasses.dataclass
class GetNotificationTargetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    




@dataclasses.dataclass
class GetNotificationTargetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    notification_targets: Optional[shared_notificationtargets.NotificationTargets] = dataclasses.field(default=None)
    r"""a list of NotificationTarget objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

