"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any

class OutputStatusStatusHealth(str, Enum):
    GREEN = 'Green'
    YELLOW = 'Yellow'
    RED = 'Red'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputStatusStatus:
    health: OutputStatusStatusHealth = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('health') }})
    metrics: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics') }})
    timestamp: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputStatus:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    status: OutputStatusStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    
