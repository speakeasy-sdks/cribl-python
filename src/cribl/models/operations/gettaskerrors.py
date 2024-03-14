"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import taskerrors as components_taskerrors
from typing import Optional


@dataclasses.dataclass
class GetTaskErrorsRequest:
    group: str = dataclasses.field(metadata={'path_param': { 'field_name': 'group', 'style': 'simple', 'explode': False }})
    r"""Group the job belongs to"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Instance id of the job to get results for"""
    



@dataclasses.dataclass
class GetTaskErrorsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    task_errors: Optional[components_taskerrors.TaskErrors] = dataclasses.field(default=None)
    r"""a list of any objects"""
    

