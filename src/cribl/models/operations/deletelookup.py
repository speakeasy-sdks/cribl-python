"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional



@dataclasses.dataclass
class DeleteLookupRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique ID"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteLookup200ApplicationJSON2:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Filename with the lookup table. Required."""
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    r"""File content."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Brief description of this lookup. Optional."""
    size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""File size. Optional."""
    tags: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    r"""One or more tags related to this lookup. Optional."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteLookup200ApplicationJSON1FileInfo:
    r"""Uploaded file information"""
    filename: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteLookup200ApplicationJSON1:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Filename with the lookup table. Required."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Brief description of this lookup. Optional."""
    file_info: Optional[DeleteLookup200ApplicationJSON1FileInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileInfo'), 'exclude': lambda f: f is None }})
    r"""Uploaded file information"""
    size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""File size. Optional."""
    tags: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    r"""One or more tags related to this lookup. Optional."""
    




@dataclasses.dataclass
class DeleteLookupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    lookup_file: Optional[Any] = dataclasses.field(default=None)
    r"""a list of LookupFile objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

