"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import packinfos as shared_packinfos
from typing import Optional



@dataclasses.dataclass
class GetPacksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    pack_infos: Optional[shared_packinfos.PackInfos] = dataclasses.field(default=None)
    r"""a list of PackInfo objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

