"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import eventbreakerrulefields as shared_eventbreakerrulefields
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class EventBreakerRuleTimestampType(str, Enum):
    AUTO = 'auto'
    FORMAT = 'format'
    CURRENT = 'current'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EventBreakerRuleTimestamp:
    type: EventBreakerRuleTimestampType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    length: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('length'), 'exclude': lambda f: f is None }})
    


class EventBreakerRuleType(str, Enum):
    REGEX = 'regex'
    JSON = 'json'
    JSON_ARRAY = 'json_array'
    HEADER = 'header'
    TIMESTAMP = 'timestamp'
    CSV = 'csv'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EventBreakerRule:
    condition: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('condition') }})
    max_event_bytes: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxEventBytes') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    timestamp: EventBreakerRuleTimestamp = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp') }})
    timestamp_anchor_regex: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampAnchorRegex') }})
    timestamp_timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampTimezone') }})
    clean_fields: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cleanFields'), 'exclude': lambda f: f is None }})
    delimiter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    delimiter_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiterRegex'), 'exclude': lambda f: f is None }})
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escapeChar'), 'exclude': lambda f: f is None }})
    event_breaker_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventBreakerRegex'), 'exclude': lambda f: f is None }})
    fields_: Optional[list[shared_eventbreakerrulefields.EventBreakerRuleFields]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})
    fields_line_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fieldsLineRegex'), 'exclude': lambda f: f is None }})
    header_line_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headerLineRegex'), 'exclude': lambda f: f is None }})
    json_array_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jsonArrayField'), 'exclude': lambda f: f is None }})
    json_extract_all: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jsonExtractAll'), 'exclude': lambda f: f is None }})
    json_time_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jsonTimeField'), 'exclude': lambda f: f is None }})
    null_field_val: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nullFieldVal'), 'exclude': lambda f: f is None }})
    parser: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parser'), 'exclude': lambda f: f is None }})
    parser_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parserEnabled'), 'exclude': lambda f: f is None }})
    quote_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quoteChar'), 'exclude': lambda f: f is None }})
    time_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeField'), 'exclude': lambda f: f is None }})
    timestamp_earliest: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampEarliest'), 'exclude': lambda f: f is None }})
    timestamp_latest: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampLatest'), 'exclude': lambda f: f is None }})
    type: Optional[EventBreakerRuleType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

