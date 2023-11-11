"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import ikmsproviderconfig as components_ikmsproviderconfig
from typing import Optional


@dataclasses.dataclass
class UpdateKMSConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ikms_provider_config: Optional[components_ikmsproviderconfig.IKMSProviderConfig] = dataclasses.field(default=None)
    r"""a list of IKMSProviderConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

