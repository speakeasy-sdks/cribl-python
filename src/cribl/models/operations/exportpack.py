"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import packinfos as shared_packinfos
from typing import Optional



@dataclasses.dataclass
class ExportPackRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Pack name"""
    mode: str = dataclasses.field(metadata={'query_param': { 'field_name': 'mode', 'style': 'form', 'explode': True }})
    r"""Export mode, one of \\"merge_safe\\", \\"merge\\", \\"default_only\\" """
    filename: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filename', 'style': 'form', 'explode': True }})
    r"""Filename of the exported Pack"""
    




@dataclasses.dataclass
class ExportPackResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    pack_infos: Optional[shared_packinfos.PackInfos] = dataclasses.field(default=None)
    r"""a list of PackInfo objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

