"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class NotificationTargetWebhookAuthenticationType(str, Enum):
    r"""The authentication method to use for the HTTP request. Defaults to None."""
    NONE = 'none'
    BASIC = 'basic'
    TOKEN = 'token'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NotificationTargetWebhookExtraHTTPHeaders:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Field name"""
    


class NotificationTargetWebhookFailedRequestLoggingMode(str, Enum):
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    PAYLOAD = 'payload'
    PAYLOAD_AND_HEADERS = 'payloadAndHeaders'
    NONE = 'none'

class NotificationTargetWebhookFormat(str, Enum):
    r"""Specifies how to format events before sending out. Defaults to NDJSON."""
    CUSTOM = 'custom'
    JSON_ARRAY = 'json_array'

class NotificationTargetWebhookMethod(str, Enum):
    r"""The method to use when sending events. Defaults to POST."""
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'

class NotificationTargetWebhookType(str, Enum):
    WEBHOOK = 'webhook'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NotificationTargetWebhook:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: NotificationTargetWebhookType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL to send events to. Can be overwritten by an event's __url field."""
    auth_type: Optional[NotificationTargetWebhookAuthenticationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""The authentication method to use for the HTTP request. Defaults to None."""
    compress: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Whether to compress the payload body before sending."""
    concurrency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking."""
    extra_http_headers: Optional[list[NotificationTargetWebhookExtraHTTPHeaders]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraHttpHeaders'), 'exclude': lambda f: f is None }})
    r"""Headers to add to all events. You can also add headers dynamically on a per-event basis in the __headers field, as explained [here](https://docs.cribl.io/stream/destinations-webhook/#internal-fields)."""
    failed_request_logging_mode: Optional[NotificationTargetWebhookFailedRequestLoggingMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRequestLoggingMode'), 'exclude': lambda f: f is None }})
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max body size."""
    format: Optional[NotificationTargetWebhookFormat] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Specifies how to format events before sending out. Defaults to NDJSON."""
    keep_alive: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keepAlive'), 'exclude': lambda f: f is None }})
    r"""Toggle to No if you want @{product} to close the connection as soon as the outgoing request is sent. Defaults to Yes."""
    max_payload_events: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Max number of events to include in the request body. Default is 0 (unlimited)."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body."""
    method: Optional[NotificationTargetWebhookMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method'), 'exclude': lambda f: f is None }})
    r"""The method to use when sending events. Defaults to POST."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    safe_headers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeHeaders'), 'exclude': lambda f: f is None }})
    r"""List of headers that are safe to log in plain text."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    timeout_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    use_round_robin_dns: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useRoundRobinDns'), 'exclude': lambda f: f is None }})
    r"""Enable to use round-robin DNS lookup. When a DNS server returns multiple addresses, this will cause Stream to cycle through them in the order returned."""
    

