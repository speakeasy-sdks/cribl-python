"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Condition:
    conf: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('__conf') }})
    filename: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('__filename') }})
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    group: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    init_time: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initTime') }})
    load_time: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loadTime') }})
    mod_time: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modTime') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    schema: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    uischema: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uischema') }})
    version: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version') }})
    

