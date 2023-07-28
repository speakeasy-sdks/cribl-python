"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import outputs as shared_outputs
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody402ExtraHTTPHeaders:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Field name"""
    


class CreateOutputObjectRequestBody402FailedRequestLoggingMode(str, Enum):
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    PAYLOAD = 'payload'
    PAYLOAD_AND_HEADERS = 'payloadAndHeaders'
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody402Labels:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the label."""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Value of the label."""
    


class CreateOutputObjectRequestBody402LokiAuthAuthenticationType(str, Enum):
    r"""The authentication method to use for the HTTP requests"""
    CREDENTIALS_SECRET = 'credentialsSecret'
    TOKEN = 'token'
    TEXT_SECRET = 'textSecret'
    BASIC = 'basic'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody402LokiAuth:
    auth_type: Optional[CreateOutputObjectRequestBody402LokiAuthAuthenticationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""The authentication method to use for the HTTP requests"""
    credentials_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentialsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a secret that references your credentials"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password (a.k.a API key in Grafana Cloud domain) for authentication"""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""Bearer token to include in the authorization header. In Grafana Cloud, this is generally built by concatenating the username and the API key, separated by a colon. E.g.: <your-username>:<your-api-key>."""
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    r"""Username for authentication"""
    


class CreateOutputObjectRequestBody402MessageFormat(str, Enum):
    r"""Which format to use when sending logs to Loki (Protobuf or JSON).  Defaults to Protobuf."""
    PROTOBUF = 'protobuf'
    JSON = 'json'

class CreateOutputObjectRequestBody402BackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class CreateOutputObjectRequestBody402Compression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class CreateOutputObjectRequestBody402PqControls:
    pass

class CreateOutputObjectRequestBody402QueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class CreateOutputObjectRequestBody402PrometheusAuthAuthenticationType(str, Enum):
    r"""The authentication method to use for the HTTP requests"""
    CREDENTIALS_SECRET = 'credentialsSecret'
    TOKEN = 'token'
    TEXT_SECRET = 'textSecret'
    BASIC = 'basic'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody402PrometheusAuth:
    auth_type: Optional[CreateOutputObjectRequestBody402PrometheusAuthAuthenticationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""The authentication method to use for the HTTP requests"""
    credentials_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentialsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a secret that references your credentials"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password (a.k.a API key in Grafana Cloud domain) for authentication"""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""Bearer token to include in the authorization header. In Grafana Cloud, this is generally built by concatenating the username and the API key, separated by a colon. E.g.: <your-username>:<your-api-key>."""
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    r"""Username for authentication"""
    


class CreateOutputObjectRequestBody402Type(str, Enum):
    GRAFANA_CLOUD = 'grafana_cloud'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody402:
    loki_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lokiUrl') }})
    r"""The endpoint to send logs to, e.g.: https://logs-prod-us-central1.grafana.net"""
    prometheus_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prometheusUrl') }})
    r"""The remote_write endpoint to send Prometheus metrics to, e.g.: https://prometheus-blocks-prod-us-central1.grafana.net/api/prom/push"""
    compress: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Whether to compress the payload body before sending. Applies only to Loki's JSON payloads, as both Prometheus' and Loki's Protobuf variant are snappy-compressed by default."""
    concurrency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking. Warning: Setting this value > 1 can cause Loki and Prometheus to complain about entries being delivered out of order."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    extra_http_headers: Optional[list[CreateOutputObjectRequestBody402ExtraHTTPHeaders]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraHttpHeaders'), 'exclude': lambda f: f is None }})
    r"""Headers to add to all events."""
    failed_request_logging_mode: Optional[CreateOutputObjectRequestBody402FailedRequestLoggingMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRequestLoggingMode'), 'exclude': lambda f: f is None }})
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Maximum time between requests. Small values can reduce the payload size below the configured 'Max record size' and 'Max events per request'. Warning: Setting this too low can increase the number of ongoing requests (depending on the value of 'Request concurrency'); this can cause Loki and Prometheus to complain about entries being delivered out of order."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    labels: Optional[list[CreateOutputObjectRequestBody402Labels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    r"""List of labels to send with logs. Labels define Loki streams, so use static labels to avoid proliferating label value combinations and streams. Can be merged and/or overridden by the event's __labels field (e.g.: '__labels: {host: \\"cribl.io\\", level: \\"error\\"}')."""
    loki_auth: Optional[CreateOutputObjectRequestBody402LokiAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lokiAuth'), 'exclude': lambda f: f is None }})
    max_payload_events: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Maximum number of events to include in the request body. Default is 0 (unlimited). Warning: Setting this too low can increase the number of ongoing requests (depending on the value of 'Request concurrency'); this can cause Loki and Prometheus to complain about entries being delivered out of order."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body. Warning: Setting this too low can increase the number of ongoing requests (depending on the value of 'Request concurrency'); this can cause Loki and Prometheus to complain about entries being delivered out of order."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Name of the event field that contains the message to send. If not specified, Stream sends a JSON representation of the whole event."""
    message_format: Optional[CreateOutputObjectRequestBody402MessageFormat] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messageFormat'), 'exclude': lambda f: f is None }})
    r"""Which format to use when sending logs to Loki (Protobuf or JSON).  Defaults to Protobuf."""
    metric_rename_expr: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricRenameExpr'), 'exclude': lambda f: f is None }})
    r"""A JS expression that can be used to rename metrics. E.g.: name.replace(/\./g, '_') will replace all '.' characters in a metric's name with the supported '_' character. Use the 'name' global variable to access the metric's name.  You can access event fields' values via __e.<fieldName>."""
    on_backpressure: Optional[CreateOutputObjectRequestBody402BackpressureBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[CreateOutputObjectRequestBody402Compression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[CreateOutputObjectRequestBody402PqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[CreateOutputObjectRequestBody402QueueFullBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    prometheus_auth: Optional[CreateOutputObjectRequestBody402PrometheusAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prometheusAuth'), 'exclude': lambda f: f is None }})
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to Yes."""
    safe_headers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeHeaders'), 'exclude': lambda f: f is None }})
    r"""List of headers that are safe to log in plain text."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported. These fields are added as dimensions and labels to generated metrics and logs respectively."""
    timeout_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    type: Optional[CreateOutputObjectRequestBody402Type] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    use_round_robin_dns: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useRoundRobinDns'), 'exclude': lambda f: f is None }})
    r"""Enable to use round-robin DNS lookup. When a DNS server returns multiple addresses, this will cause Stream to cycle through them in the order returned."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody401ExtraHTTPHeaders:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Field name"""
    


class CreateOutputObjectRequestBody401FailedRequestLoggingMode(str, Enum):
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    PAYLOAD = 'payload'
    PAYLOAD_AND_HEADERS = 'payloadAndHeaders'
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody401Labels:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the label."""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Value of the label."""
    


class CreateOutputObjectRequestBody401LokiAuthAuthenticationType(str, Enum):
    r"""The authentication method to use for the HTTP requests"""
    CREDENTIALS_SECRET = 'credentialsSecret'
    TOKEN = 'token'
    TEXT_SECRET = 'textSecret'
    BASIC = 'basic'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody401LokiAuth:
    auth_type: Optional[CreateOutputObjectRequestBody401LokiAuthAuthenticationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""The authentication method to use for the HTTP requests"""
    credentials_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentialsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a secret that references your credentials"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password (a.k.a API key in Grafana Cloud domain) for authentication"""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""Bearer token to include in the authorization header. In Grafana Cloud, this is generally built by concatenating the username and the API key, separated by a colon. E.g.: <your-username>:<your-api-key>."""
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    r"""Username for authentication"""
    


class CreateOutputObjectRequestBody401MessageFormat(str, Enum):
    r"""Which format to use when sending logs to Loki (Protobuf or JSON).  Defaults to Protobuf."""
    PROTOBUF = 'protobuf'
    JSON = 'json'

class CreateOutputObjectRequestBody401BackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class CreateOutputObjectRequestBody401Compression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class CreateOutputObjectRequestBody401PqControls:
    pass

class CreateOutputObjectRequestBody401QueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class CreateOutputObjectRequestBody401PrometheusAuthAuthenticationType(str, Enum):
    r"""The authentication method to use for the HTTP requests"""
    CREDENTIALS_SECRET = 'credentialsSecret'
    TOKEN = 'token'
    TEXT_SECRET = 'textSecret'
    BASIC = 'basic'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody401PrometheusAuth:
    auth_type: Optional[CreateOutputObjectRequestBody401PrometheusAuthAuthenticationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""The authentication method to use for the HTTP requests"""
    credentials_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentialsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a secret that references your credentials"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password (a.k.a API key in Grafana Cloud domain) for authentication"""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""Bearer token to include in the authorization header. In Grafana Cloud, this is generally built by concatenating the username and the API key, separated by a colon. E.g.: <your-username>:<your-api-key>."""
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    r"""Username for authentication"""
    


class CreateOutputObjectRequestBody401Type(str, Enum):
    GRAFANA_CLOUD = 'grafana_cloud'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOutputObjectRequestBody401:
    loki_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lokiUrl') }})
    r"""The endpoint to send logs to, e.g.: https://logs-prod-us-central1.grafana.net"""
    prometheus_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prometheusUrl') }})
    r"""The remote_write endpoint to send Prometheus metrics to, e.g.: https://prometheus-blocks-prod-us-central1.grafana.net/api/prom/push"""
    compress: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Whether to compress the payload body before sending. Applies only to Loki's JSON payloads, as both Prometheus' and Loki's Protobuf variant are snappy-compressed by default."""
    concurrency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking. Warning: Setting this value > 1 can cause Loki and Prometheus to complain about entries being delivered out of order."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    extra_http_headers: Optional[list[CreateOutputObjectRequestBody401ExtraHTTPHeaders]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraHttpHeaders'), 'exclude': lambda f: f is None }})
    r"""Headers to add to all events."""
    failed_request_logging_mode: Optional[CreateOutputObjectRequestBody401FailedRequestLoggingMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRequestLoggingMode'), 'exclude': lambda f: f is None }})
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Maximum time between requests. Small values can reduce the payload size below the configured 'Max record size' and 'Max events per request'. Warning: Setting this too low can increase the number of ongoing requests (depending on the value of 'Request concurrency'); this can cause Loki and Prometheus to complain about entries being delivered out of order."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    labels: Optional[list[CreateOutputObjectRequestBody401Labels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    r"""List of labels to send with logs. Labels define Loki streams, so use static labels to avoid proliferating label value combinations and streams. Can be merged and/or overridden by the event's __labels field (e.g.: '__labels: {host: \\"cribl.io\\", level: \\"error\\"}')."""
    loki_auth: Optional[CreateOutputObjectRequestBody401LokiAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lokiAuth'), 'exclude': lambda f: f is None }})
    max_payload_events: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Maximum number of events to include in the request body. Default is 0 (unlimited). Warning: Setting this too low can increase the number of ongoing requests (depending on the value of 'Request concurrency'); this can cause Loki and Prometheus to complain about entries being delivered out of order."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body. Warning: Setting this too low can increase the number of ongoing requests (depending on the value of 'Request concurrency'); this can cause Loki and Prometheus to complain about entries being delivered out of order."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Name of the event field that contains the message to send. If not specified, Stream sends a JSON representation of the whole event."""
    message_format: Optional[CreateOutputObjectRequestBody401MessageFormat] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messageFormat'), 'exclude': lambda f: f is None }})
    r"""Which format to use when sending logs to Loki (Protobuf or JSON).  Defaults to Protobuf."""
    metric_rename_expr: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricRenameExpr'), 'exclude': lambda f: f is None }})
    r"""A JS expression that can be used to rename metrics. E.g.: name.replace(/\./g, '_') will replace all '.' characters in a metric's name with the supported '_' character. Use the 'name' global variable to access the metric's name.  You can access event fields' values via __e.<fieldName>."""
    on_backpressure: Optional[CreateOutputObjectRequestBody401BackpressureBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[CreateOutputObjectRequestBody401Compression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[CreateOutputObjectRequestBody401PqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[CreateOutputObjectRequestBody401QueueFullBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    prometheus_auth: Optional[CreateOutputObjectRequestBody401PrometheusAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prometheusAuth'), 'exclude': lambda f: f is None }})
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to Yes."""
    safe_headers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeHeaders'), 'exclude': lambda f: f is None }})
    r"""List of headers that are safe to log in plain text."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported. These fields are added as dimensions and labels to generated metrics and logs respectively."""
    timeout_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    type: Optional[CreateOutputObjectRequestBody401Type] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    use_round_robin_dns: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useRoundRobinDns'), 'exclude': lambda f: f is None }})
    r"""Enable to use round-robin DNS lookup. When a DNS server returns multiple addresses, this will cause Stream to cycle through them in the order returned."""
    




@dataclasses.dataclass
class CreateOutputObjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    outputs: Optional[shared_outputs.Outputs] = dataclasses.field(default=None)
    r"""a list of Output objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
