"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import roles as components_roles
from typing import Optional


@dataclasses.dataclass
class CreateRoleResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    roles: Optional[components_roles.Roles] = dataclasses.field(default=None)
    r"""a list of Role objects"""
    

