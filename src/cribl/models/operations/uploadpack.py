"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import packinfos as components_packinfos
from typing import Optional


@dataclasses.dataclass
class UploadPackRequest:
    filename: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filename', 'style': 'form', 'explode': True }})
    r"""the file to upload"""
    



@dataclasses.dataclass
class UploadPackResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    pack_infos: Optional[components_packinfos.PackInfos] = dataclasses.field(default=None)
    r"""a list of PackInfo objects"""
    

