"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import eventbreakerrule as shared_eventbreakerrule
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DatatypePreviewRequestBody:
    r"""DatatypePreviewRequestBody object"""
    input: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input') }})
    event_breaker_rule: Optional[shared_eventbreakerrule.EventBreakerRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventBreakerRule'), 'exclude': lambda f: f is None }})
    

