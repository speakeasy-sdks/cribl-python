"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional

class OutputGoogleCloudLoggingAuthenticationMethod(str, Enum):
    r"""Google authentication method. Choose Auto to use environment variable GOOGLE_APPLICATION_CREDENTIALS.."""
    SECRET = 'secret'
    MANUAL = 'manual'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputGoogleCloudLoggingLogLabels:
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    r"""Label name"""
    value_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('valueExpression') }})
    r"""JavaScript expression to compute the label's value."""
    


class OutputGoogleCloudLoggingLogLocationType(str, Enum):
    FOLDER = 'folder'
    ORGANIZATION = 'organization'
    BILLING_ACCOUNT = 'billingAccount'

class OutputGoogleCloudLoggingBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputGoogleCloudLoggingPayloadFormat(str, Enum):
    r"""Format to use when sending payload. Defaults to Text."""
    JSON = 'json'
    TEXT = 'text'

class OutputGoogleCloudLoggingCompression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'


@dataclasses.dataclass
class OutputGoogleCloudLoggingPqControls:
    pass

class OutputGoogleCloudLoggingQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputGoogleCloudLoggingResourceTypeLabels:
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    r"""Label name"""
    value_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('valueExpression') }})
    r"""JavaScript expression to compute the label's value."""
    


class OutputGoogleCloudLoggingType(str, Enum):
    GOOGLE_CLOUD_LOGGING = 'google_cloud_logging'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputGoogleCloudLogging:
    log_location_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logLocationExpression') }})
    r"""JavaScript expression to compute the value of the folder ID with which log entries should be associated."""
    log_location_type: OutputGoogleCloudLoggingLogLocationType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logLocationType') }})
    log_name_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logNameExpression') }})
    r"""JavaScript expression to compute the value of the log name."""
    concurrency: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking."""
    connection_timeout: Optional[int] = dataclasses.field(default=10000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for the connection to establish before retrying"""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    flush_period_sec: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max record size."""
    google_auth_method: Optional[OutputGoogleCloudLoggingAuthenticationMethod] = dataclasses.field(default=OutputGoogleCloudLoggingAuthenticationMethod.MANUAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('googleAuthMethod'), 'exclude': lambda f: f is None }})
    r"""Google authentication method. Choose Auto to use environment variable GOOGLE_APPLICATION_CREDENTIALS.."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    insert_id_expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insertIdExpression'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to compute the value of the insert ID field."""
    log_labels: Optional[List[OutputGoogleCloudLoggingLogLabels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logLabels'), 'exclude': lambda f: f is None }})
    r"""Labels to apply to the log entry"""
    max_payload_events: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Max number of events to include in the request body. Default is 0 (unlimited)."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=4096, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body."""
    on_backpressure: Optional[OutputGoogleCloudLoggingBackpressureBehavior] = dataclasses.field(default=OutputGoogleCloudLoggingBackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    payload_expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payloadExpression'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to compute the value of the payload. Must evaluate to a JavaScript object value. If an invalid value is encountered it will result in the default value instead. Defaults to the entire event."""
    payload_format: Optional[OutputGoogleCloudLoggingPayloadFormat] = dataclasses.field(default=OutputGoogleCloudLoggingPayloadFormat.TEXT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payloadFormat'), 'exclude': lambda f: f is None }})
    r"""Format to use when sending payload. Defaults to Text."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputGoogleCloudLoggingCompression] = dataclasses.field(default=OutputGoogleCloudLoggingCompression.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputGoogleCloudLoggingPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default='1 MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputGoogleCloudLoggingQueueFullBehavior] = dataclasses.field(default=OutputGoogleCloudLoggingQueueFullBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/queues', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    resource_type_expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceTypeExpression'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to compute the value of the managed resource type field. Must evaluate to one of the valid values [here](https://cloud.google.com/logging/docs/api/v2/resource-list#resource-types). Defaults to \\"global\\"."""
    resource_type_labels: Optional[List[OutputGoogleCloudLoggingResourceTypeLabels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceTypeLabels'), 'exclude': lambda f: f is None }})
    r"""Labels to apply to the managed resource. These must correspond to the valid labels for the specified resource type (see [here](https://cloud.google.com/logging/docs/api/v2/resource-list#resource-types)). Otherwise, they will be dropped by Google Cloud Logging."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    service_account_credentials: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serviceAccountCredentials'), 'exclude': lambda f: f is None }})
    r"""Contents of service account credentials (JSON keys) file downloaded from Google Cloud. To upload a file, click the upload button at this field's upper right. As an alternative, you can use environment variables (see [here](https://cloud.google.com/docs/authentication/provide-credentials-adc))."""
    severity_expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severityExpression'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to compute the value of the severity field. Must evaluate to one of the severity values supported by Google Cloud Logging [here](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) (case insensitive). Defaults to \\"DEFAULT\\"."""
    streamtags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    throttle_rate_req_per_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throttleRateReqPerSec'), 'exclude': lambda f: f is None }})
    r"""Maximum number of requests to limit to per second."""
    timeout_sec: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    type: Optional[OutputGoogleCloudLoggingType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

