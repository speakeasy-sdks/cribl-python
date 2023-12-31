"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class NotificationTargetBaseOutputType(str, Enum):
    DEFAULT = 'default'
    WEBHOOK = 'webhook'
    BULLETIN_MESSAGE = 'bulletin_message'
    ROUTER = 'router'
    NOTIFICATIONS_LOG = 'notifications_log'
    PAGER_DUTY = 'pager_duty'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NotificationTargetBase:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: NotificationTargetBaseOutputType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    

