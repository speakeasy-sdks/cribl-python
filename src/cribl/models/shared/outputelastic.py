"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class OutputElasticAuthAuthenticationMethod(str, Enum):
    r"""Enter credentials directly, or select a stored secret"""
    MANUAL = 'manual'
    SECRET = 'secret'
    MANUAL_API_KEY = 'manualAPIKey'
    TEXT_SECRET = 'textSecret'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputElasticAuth:
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    auth_type: Optional[OutputElasticAuthAuthenticationMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""Enter credentials directly, or select a stored secret"""
    


class OutputElasticElasticVersion(str, Enum):
    r"""Optional Elasticsearch version, used to format events. If not specified, will auto-discover version."""
    AUTO = 'auto'
    SIX = '6'
    SEVEN = '7'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputElasticExtraHTTPHeaders:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Field name"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputElasticExtraParams:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Field name"""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Field value"""
    


class OutputElasticFailedRequestLoggingMode(str, Enum):
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    PAYLOAD = 'payload'
    PAYLOAD_AND_HEADERS = 'payloadAndHeaders'
    NONE = 'none'

class OutputElasticBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputElasticOptionalFieldsInGeneralSection(str, Enum):
    LOAD_BALANCED = 'loadBalanced'
    URLS = 'urls'

class OutputElasticCompression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class OutputElasticPqControls:
    pass

class OutputElasticQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputElasticType(str, Enum):
    ELASTIC = 'elastic'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputElasticUrls:
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL to an Elastic node to send events to – e.g., http://elastic:9200/_bulk"""
    weight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    r"""The weight to use for load-balancing purposes."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputElastic:
    index: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    r"""Index or Data Stream to send events to. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be overwritten by an event's __index field."""
    type: OutputElasticType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    auth: Optional[OutputElasticAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth'), 'exclude': lambda f: f is None }})
    compress: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Whether to compress the payload body before sending."""
    concurrency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency'), 'exclude': lambda f: f is None }})
    r"""Maximum number of ongoing requests before blocking."""
    dns_resolve_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dnsResolvePeriodSec'), 'exclude': lambda f: f is None }})
    r"""Re-resolve any hostnames every this many seconds and pick up destinations from A records."""
    doc_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('docType'), 'exclude': lambda f: f is None }})
    r"""Document type to use for events. Can be overwritten by an event's __type field"""
    elastic_pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('elasticPipeline'), 'exclude': lambda f: f is None }})
    r"""Optional Elasticsearch destination pipeline"""
    elastic_version: Optional[OutputElasticElasticVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('elasticVersion'), 'exclude': lambda f: f is None }})
    r"""Optional Elasticsearch version, used to format events. If not specified, will auto-discover version."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    exclude_self: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeSelf'), 'exclude': lambda f: f is None }})
    r"""Exclude all IPs of the current host from the list of any resolved hostnames."""
    extra_http_headers: Optional[list[OutputElasticExtraHTTPHeaders]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraHttpHeaders'), 'exclude': lambda f: f is None }})
    r"""Headers to add to all events."""
    extra_params: Optional[list[OutputElasticExtraParams]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extraParams'), 'exclude': lambda f: f is None }})
    r"""Extra Parameters."""
    failed_request_logging_mode: Optional[OutputElasticFailedRequestLoggingMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRequestLoggingMode'), 'exclude': lambda f: f is None }})
    r"""Determines which data should be logged when a request fails. Defaults to None.  All headers are redacted by default, except those listed under `Safe Headers`."""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max body size."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    include_doc_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('includeDocId'), 'exclude': lambda f: f is None }})
    r"""Toggle this off when sending events to an Elastic TSDS (time series data stream)"""
    load_balanced: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loadBalanced'), 'exclude': lambda f: f is None }})
    r"""Use load-balanced destinations"""
    load_balance_stats_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loadBalanceStatsPeriodSec'), 'exclude': lambda f: f is None }})
    r"""How far back in time to keep traffic stats for load balancing purposes."""
    max_payload_events: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadEvents'), 'exclude': lambda f: f is None }})
    r"""Max number of events to include in the request body. Default is 0 (unlimited)."""
    max_payload_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxPayloadSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size, in KB, of the request body."""
    on_backpressure: Optional[OutputElasticBackpressureBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    optional_fields_in_general_section: Optional[OutputElasticOptionalFieldsInGeneralSection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optionalFieldsInGeneralSection'), 'exclude': lambda f: f is None }})
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputElasticCompression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputElasticPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputElasticQueueFullBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    safe_headers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeHeaders'), 'exclude': lambda f: f is None }})
    r"""List of headers that are safe to log in plain text."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    timeout_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSec'), 'exclude': lambda f: f is None }})
    r"""Amount of time, in seconds, to wait for a request to complete before aborting it."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""Enter Cloud ID or URL to an Elastic cluster to send events to – e.g., http://elastic:9200/_bulk"""
    urls: Optional[list[OutputElasticUrls]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('urls'), 'exclude': lambda f: f is None }})
    use_round_robin_dns: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useRoundRobinDns'), 'exclude': lambda f: f is None }})
    r"""Enable to use round-robin DNS lookup. When a DNS server returns multiple addresses, this will cause Stream to cycle through them in the order returned."""
    

