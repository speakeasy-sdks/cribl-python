"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class HealthStatusStatus(str, Enum):
    HEALTHY = 'healthy'
    SHUTTING_DOWN = 'shutting down'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class HealthStatus:
    r"""Healthy"""
    status: HealthStatusStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

