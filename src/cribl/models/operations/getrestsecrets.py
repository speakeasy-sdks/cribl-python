"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import restsecrets as shared_restsecrets
from typing import Optional



@dataclasses.dataclass
class GetRestSecretsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    rest_secrets: Optional[shared_restsecrets.RestSecrets] = dataclasses.field(default=None)
    r"""a list of RestSecret objects"""
    

