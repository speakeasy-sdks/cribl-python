"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dockergraphdriverdata as shared_dockergraphdriverdata
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DockerGraphDriver:
    data: Optional[shared_dockergraphdriverdata.DockerGraphDriverData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Data'), 'exclude': lambda f: f is None }})
    

