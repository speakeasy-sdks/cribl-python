"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional



@dataclasses.dataclass
class GetLatestPQRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Output Id"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetLatestPQ200ApplicationJSON:
    r"""a list of any objects"""
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    r"""number of items present in the items array"""
    items: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetLatestPQResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_latest_pq_200_application_json_object: Optional[GetLatestPQ200ApplicationJSON] = dataclasses.field(default=None)
    r"""a list of any objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
