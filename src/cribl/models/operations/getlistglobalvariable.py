"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import globalvars as shared_globalvars
from typing import Optional



@dataclasses.dataclass
class GetListGlobalVariableResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    global_vars: Optional[shared_globalvars.GlobalVars] = dataclasses.field(default=None)
    r"""a list of Global Variable objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

