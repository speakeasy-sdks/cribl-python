"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class OutputDatasetAuthenticationMethod(str, Enum):
    r"""Enter API key directly, or select a stored secret"""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputDatasetSeverity(str, Enum):
    r"""Default value for event severity. If the `sev` or `__severity` fields are set on an event, the first one matching will override this value."""
    FINEST = 'finest'
    FINER = 'finer'
    FINE = 'fine'
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    FATAL = 'fatal'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputDatasetExtraHTTPHeaders:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Field name"""
    


class OutputDatasetFailedRequestLoggingMode(str, Enum):
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    PAYLOAD = 'payload'
    PAYLOAD_AND_HEADERS = 'payloadAndHeaders'
    NONE = 'none'

class OutputDatasetBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputDatasetCompression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class OutputDatasetPqControls:
    pass

class OutputDatasetQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputDatasetDataSetSite(str, Enum):
    r"""DataSet site to which events should be sent"""
    US = 'us'
    EU = 'eu'
    CUSTOM = 'custom'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputDataset:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    TYPE: Final[str] = dataclasses.field(default='dataset', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey'), 'exclude': lambda f: f is None }})
    r"""A 'Log Write Access' API key for the DataSet account"""
    auth_type: Optional[OutputDatasetAuthenticationMethod] = dataclasses.field(default=OutputDatasetAuthenticationMethod.MANUAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""Enter API key directly, or select a stored secret"""
    compress: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Whether to compress the payload body before sending."""
    concurrency: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking."""
    custom_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customUrl'), 'exclude': lambda f: f is None }})
    default_severity: Optional[OutputDatasetSeverity] = dataclasses.field(default=OutputDatasetSeverity.INFO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultSeverity'), 'exclude': lambda f: f is None }})
    r"""Default value for event severity. If the `sev` or `__severity` fields are set on an event, the first one matching will override this value."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    exclude_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeFields'), 'exclude': lambda f: f is None }})
    r"""Fields to exclude from the event if the Message field is either unspecified or refers to an object. Ignored if the Message field is a string. If empty, we send all non-internal fields."""
    extra_http_headers: Optional[list[OutputDatasetExtraHTTPHeaders]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraHttpHeaders'), 'exclude': lambda f: f is None }})
    r"""Headers to add to all events."""
    failed_request_logging_mode: Optional[OutputDatasetFailedRequestLoggingMode] = dataclasses.field(default=OutputDatasetFailedRequestLoggingMode.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRequestLoggingMode'), 'exclude': lambda f: f is None }})
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    flush_period_sec: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max body size."""
    max_payload_events: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Max number of events to include in the request body. Default is 0 (unlimited)."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=4096, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body."""
    message_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messageField'), 'exclude': lambda f: f is None }})
    r"""Name of the event field that contains the message or attributes to send. If not specified, all of the event's non-internal fields will be sent as attributes."""
    on_backpressure: Optional[OutputDatasetBackpressureBehavior] = dataclasses.field(default=OutputDatasetBackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputDatasetCompression] = dataclasses.field(default=OutputDatasetCompression.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputDatasetPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default='1 MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputDatasetQueueFullBehavior] = dataclasses.field(default=OutputDatasetQueueFullBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/queues', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to Yes."""
    safe_headers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeHeaders'), 'exclude': lambda f: f is None }})
    r"""List of headers that are safe to log in plain text."""
    server_host_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serverHostField'), 'exclude': lambda f: f is None }})
    r"""Name of the event field that contains the `serverHost` identifier. If not specified, defaults to `cribl_<outputId>`."""
    site: Optional[OutputDatasetDataSetSite] = dataclasses.field(default=OutputDatasetDataSetSite.US, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site'), 'exclude': lambda f: f is None }})
    r"""DataSet site to which events should be sent"""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    timeout_sec: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    timestamp_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampField'), 'exclude': lambda f: f is None }})
    r"""Name of the event field that contains the timestamp. If not specified, defaults to `ts`, `_time`, or `Date.now()`, in that order."""
    use_round_robin_dns: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useRoundRobinDns'), 'exclude': lambda f: f is None }})
    r"""Enable to use round-robin DNS lookup. When a DNS server returns multiple addresses, this will cause Stream to cycle through them in the order returned."""
    

