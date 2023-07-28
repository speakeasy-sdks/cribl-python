"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import kmsconfigs as shared_kmsconfigs
from typing import Optional



@dataclasses.dataclass
class GetKMSConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    kms_configs: Optional[shared_kmsconfigs.KMSConfigs] = dataclasses.field(default=None)
    r"""a list of IKMSProviderConfig objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
