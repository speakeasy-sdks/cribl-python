"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchsettingses as shared_searchsettingses
from typing import Optional



@dataclasses.dataclass
class GetSearchLimitsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    search_settingses: Optional[shared_searchsettingses.SearchSettingses] = dataclasses.field(default=None)
    r"""a list of SearchSettings objects"""
    
