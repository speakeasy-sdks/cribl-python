"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.errors import success as errors_success
from typing import Optional


@dataclasses.dataclass
class PostRequestAuthRequestBody:
    r"""Authentication request object"""
    relay_state: Optional[str] = dataclasses.field(default=None, metadata={'form': { 'field_name': 'RelayState' }})
    saml_response: Optional[str] = dataclasses.field(default=None, metadata={'form': { 'field_name': 'SAMLResponse' }})
    r"""Authentication request object"""
    



@dataclasses.dataclass
class PostRequestAuthResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    success: Optional[errors_success.Success] = dataclasses.field(default=None)
    r"""Authentication success"""
    

