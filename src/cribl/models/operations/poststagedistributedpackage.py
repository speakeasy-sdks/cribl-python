"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import criblpackage as components_criblpackage
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class PostStageDistributedPackageRequest:
    group: str = dataclasses.field(metadata={'path_param': { 'field_name': 'group', 'style': 'simple', 'explode': False }})
    r"""Group to upgrade"""
    upgrade_percentage: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'upgradePercentage', 'style': 'form', 'explode': True }})
    r"""body number percentage of nodes on the worker group to upgrade"""
    



@dataclasses.dataclass
class PostStageDistributedPackageResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    cribl_package: Optional[components_criblpackage.CriblPackage] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

