"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .commonservicelimitconfigs import CommonServiceLimitConfigs
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServicesLimits:
    connections: CommonServiceLimitConfigs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connections') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    metrics: CommonServiceLimitConfigs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics') }})
    notifications: CommonServiceLimitConfigs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notifications') }})
    
