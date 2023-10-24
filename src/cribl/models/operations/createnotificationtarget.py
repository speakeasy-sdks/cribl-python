"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import notificationtargets as shared_notificationtargets
from typing import Optional


@dataclasses.dataclass
class CreateNotificationTargetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    notification_targets: Optional[shared_notificationtargets.NotificationTargets] = dataclasses.field(default=None)
    r"""a list of NotificationTarget objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

