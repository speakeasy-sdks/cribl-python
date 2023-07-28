"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class NotificationTargetPagerDutySeverity(str, Enum):
    r"""Default value for message severity, will be overwritten by value of __severity if set. Defaults to info."""
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    CRITICAL = 'critical'

class NotificationTargetPagerDutyType(str, Enum):
    PAGER_DUTY = 'pager_duty'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NotificationTargetPagerDuty:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    routing_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingKey') }})
    r"""This is the 32 character Integration Key for an integration on a service or on a global ruleset."""
    type: NotificationTargetPagerDutyType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    class_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('class'), 'exclude': lambda f: f is None }})
    r"""Optional, default class value"""
    component: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('component'), 'exclude': lambda f: f is None }})
    r"""Optional, default component value"""
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    r"""Optional, default group value"""
    severity: Optional[NotificationTargetPagerDutySeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""Default value for message severity, will be overwritten by value of __severity if set. Defaults to info."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    
