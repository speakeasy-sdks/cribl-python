"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Dict, List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputSamplesResponse:
    events: List[Dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    
