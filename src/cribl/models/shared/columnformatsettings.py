"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ColumnFormatSettings:
    palette: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('palette') }})
    precision: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('precision') }})
    prefix: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix') }})
    suffix: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suffix') }})
    

