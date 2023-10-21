"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import changelogstateses as shared_changelogstateses
from typing import Optional


@dataclasses.dataclass
class UpdateChangelogViewStateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    changelog_stateses: Optional[shared_changelogstateses.ChangelogStateses] = dataclasses.field(default=None)
    r"""a list of ChangelogState objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

