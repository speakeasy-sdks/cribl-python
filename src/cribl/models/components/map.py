"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclasses.dataclass
class Op:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Map:
    op: Op = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('op') }})
    
