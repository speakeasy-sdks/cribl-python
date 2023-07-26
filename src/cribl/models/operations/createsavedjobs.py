"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import savedjobs as shared_savedjobs
from typing import Optional



@dataclasses.dataclass
class CreateSavedJobsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    saved_jobs: Optional[shared_savedjobs.SavedJobs] = dataclasses.field(default=None)
    r"""a list of SavedJob objects"""
    

