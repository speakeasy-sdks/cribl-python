"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crudentitybases as shared_crudentitybases
from typing import Optional



@dataclasses.dataclass
class GetListAuthGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    crud_entity_bases: Optional[shared_crudentitybases.CrudEntityBases] = dataclasses.field(default=None)
    r"""a list of CrudEntityBase objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

