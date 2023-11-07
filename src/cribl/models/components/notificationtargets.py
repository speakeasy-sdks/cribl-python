"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, List, Optional

class SchemasSeverity(str, Enum):
    r"""Default value for message severity, will be overwritten by value of __severity if set. Defaults to info."""
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    CRITICAL = 'critical'

class SchemasNotificationTargetPagerDutyType(str, Enum):
    PAGER_DUTY = 'pager_duty'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargetPagerDutySchemas:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    routing_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingKey') }})
    r"""This is the 32 character Integration Key for an integration on a service or on a global ruleset."""
    type: SchemasNotificationTargetPagerDutyType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    class_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('class'), 'exclude': lambda f: f is None }})
    r"""Optional, default class value"""
    component: Optional[str] = dataclasses.field(default='logstream', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('component'), 'exclude': lambda f: f is None }})
    r"""Optional, default component value"""
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    r"""Optional, default group value"""
    severity: Optional[SchemasSeverity] = dataclasses.field(default=SchemasSeverity.INFO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""Default value for message severity, will be overwritten by value of __severity if set. Defaults to info."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    


class SchemasNotificationTargetNotificationsLogType(str, Enum):
    NOTIFICATIONS_LOG = 'notifications_log'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargetNotificationsLogSchemas:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: SchemasNotificationTargetNotificationsLogType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    logs_dir: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logsDir'), 'exclude': lambda f: f is None }})
    r"""Directory in which to store the notification log"""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Rules:
    filter: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter') }})
    r"""JavaScript expression to select events to send to output"""
    output: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output') }})
    r"""Output to send matching events to"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of this rule's purpose"""
    final: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('final'), 'exclude': lambda f: f is None }})
    r"""Flag to control whether to stop the event from being checked against other rules"""
    


class SchemasNotificationTargetRouterType(str, Enum):
    ROUTER = 'router'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargetRouterSchemas:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    rules: List[Rules] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules') }})
    r"""Event routing rules"""
    type: SchemasNotificationTargetRouterType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    


class Severity(str, Enum):
    r"""Default value for message severity, will be overwritten by value of __severity if set. Defaults to warn."""
    ERROR = 'error'
    WARN = 'warn'
    INFO = 'info'
    FATAL = 'fatal'

class Type(str, Enum):
    BULLETIN_MESSAGE = 'bulletin_message'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargetBulletinMessageSchemas:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    severity: Optional[Severity] = dataclasses.field(default=Severity.WARN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""Default value for message severity, will be overwritten by value of __severity if set. Defaults to warn."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    text: Optional[str] = dataclasses.field(default='Notification has been triggered', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Text of the message"""
    title: Optional[str] = dataclasses.field(default='Notification', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""Title of the message"""
    


class AuthenticationType(str, Enum):
    r"""The authentication method to use for the HTTP request. Defaults to None."""
    NONE = 'none'
    BASIC = 'basic'
    TOKEN = 'token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExtraHTTPHeaders:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Field name"""
    


class FailedRequestLoggingMode(str, Enum):
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    PAYLOAD = 'payload'
    PAYLOAD_AND_HEADERS = 'payloadAndHeaders'
    NONE = 'none'

class Format(str, Enum):
    r"""Specifies how to format events before sending out. Defaults to NDJSON."""
    CUSTOM = 'custom'
    JSON_ARRAY = 'json_array'

class Method(str, Enum):
    r"""The method to use when sending events. Defaults to POST."""
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'

class SchemasNotificationTargetWebhookType(str, Enum):
    WEBHOOK = 'webhook'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargetWebhookSchemas:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: SchemasNotificationTargetWebhookType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL to send events to. Can be overwritten by an event's __url field."""
    auth_type: Optional[AuthenticationType] = dataclasses.field(default=AuthenticationType.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""The authentication method to use for the HTTP request. Defaults to None."""
    compress: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Whether to compress the payload body before sending."""
    concurrency: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking."""
    extra_http_headers: Optional[List[ExtraHTTPHeaders]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraHttpHeaders'), 'exclude': lambda f: f is None }})
    r"""Headers to add to all events. You can also add headers dynamically on a per-event basis in the __headers field, as explained [here](https://docs.cribl.io/stream/destinations-webhook/#internal-fields)."""
    failed_request_logging_mode: Optional[FailedRequestLoggingMode] = dataclasses.field(default=FailedRequestLoggingMode.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRequestLoggingMode'), 'exclude': lambda f: f is None }})
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    flush_period_sec: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max body size."""
    format: Optional[Format] = dataclasses.field(default=Format.JSON_ARRAY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Specifies how to format events before sending out. Defaults to NDJSON."""
    keep_alive: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keepAlive'), 'exclude': lambda f: f is None }})
    r"""Toggle to No if you want @{product} to close the connection as soon as the outgoing request is sent. Defaults to Yes."""
    max_payload_events: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Max number of events to include in the request body. Default is 0 (unlimited)."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=4096, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body."""
    method: Optional[Method] = dataclasses.field(default=Method.POST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method'), 'exclude': lambda f: f is None }})
    r"""The method to use when sending events. Defaults to POST."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    safe_headers: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeHeaders'), 'exclude': lambda f: f is None }})
    r"""List of headers that are safe to log in plain text."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    timeout_sec: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    use_round_robin_dns: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useRoundRobinDns'), 'exclude': lambda f: f is None }})
    r"""Enable to use round-robin DNS lookup. When a DNS server returns multiple addresses, this will cause Stream to cycle through them in the order returned."""
    


class SchemasType(str, Enum):
    DEFAULT = 'default'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargetDefaultSchemas:
    default_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultId') }})
    r"""ID of the default output. This will be used whenever a nonexistent/deleted output is referenced."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: SchemasType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    


class OutputType(str, Enum):
    DEFAULT = 'default'
    WEBHOOK = 'webhook'
    BULLETIN_MESSAGE = 'bulletin_message'
    ROUTER = 'router'
    NOTIFICATIONS_LOG = 'notifications_log'
    PAGER_DUTY = 'pager_duty'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Schemas:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: OutputType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationTargets:
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    r"""number of items present in the items array"""
    items: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    
