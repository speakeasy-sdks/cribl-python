"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SystemConf:
    install_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installType') }})
    restart: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('restart') }})
    upgrade: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upgrade') }})
    

