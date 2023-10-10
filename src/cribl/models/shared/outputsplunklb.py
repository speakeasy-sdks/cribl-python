"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class OutputSplunkLbAuthenticationMethod(str, Enum):
    r"""Enter a token directly, or provide a secret referencing a token"""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputSplunkLbHostsTLS(str, Enum):
    r"""Whether to inherit TLS configs from group setting or disable TLS."""
    INHERIT = 'inherit'
    OFF = 'off'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputSplunkLbHosts:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The hostname of the receiver."""
    port: Optional[int] = dataclasses.field(default=9997, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The port to connect to on the provided host."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Servername to use if establishing a TLS connection. If not specified, defaults to connection host (iff not an IP); otherwise, to the global TLS settings."""
    tls: Optional[OutputSplunkLbHostsTLS] = dataclasses.field(default=OutputSplunkLbHostsTLS.INHERIT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    r"""Whether to inherit TLS configs from group setting or disable TLS."""
    weight: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    r"""The weight to use for load-balancing purposes."""
    


class OutputSplunkLbIndexerDiscoveryConfigsAuthenticationMethod(str, Enum):
    r"""Enter a token directly, or provide a secret referencing a token"""
    SECRET = 'secret'
    MANUAL = 'manual'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputSplunkLbIndexerDiscoveryConfigs:
    r"""List of configurations to set up indexer discovery in Splunk Indexer clustering environment."""
    master_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('masterUri') }})
    r"""Full URI of Splunk cluster Manager (scheme://host:port). E.g.: https://managerAddress:8089"""
    auth_token: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authToken'), 'exclude': lambda f: f is None }})
    r"""Authentication token required to authenticate to cluster Manager for indexer discovery."""
    auth_type: Optional[OutputSplunkLbIndexerDiscoveryConfigsAuthenticationMethod] = dataclasses.field(default=OutputSplunkLbIndexerDiscoveryConfigsAuthenticationMethod.MANUAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""Enter a token directly, or provide a secret referencing a token"""
    refresh_interval_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refreshIntervalSec'), 'exclude': lambda f: f is None }})
    r"""Time interval in seconds between two consecutive indexer list fetches from cluster Manager."""
    site: Optional[str] = dataclasses.field(default='default', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site'), 'exclude': lambda f: f is None }})
    r"""Clustering site of the indexers from where indexers need to be discovered. In case of single site cluster, it defaults to 'default' site."""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    


class OutputSplunkLbMaxS2SVersion(str, Enum):
    r"""The highest S2S protocol version to advertise during handshake."""
    V3 = 'v3'
    V4 = 'v4'

class OutputSplunkLbNestedFieldSerialization(str, Enum):
    r"""Specifies how to serialize nested fields into index-time fields."""
    JSON = 'json'
    NONE = 'none'

class OutputSplunkLbBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputSplunkLbOptionalFieldsInGeneralSection(str, Enum):
    INDEXER_DISCOVERY = 'indexerDiscovery'
    INDEXER_DISCOVERY_CONFIGS = 'indexerDiscoveryConfigs'

class OutputSplunkLbCompression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class OutputSplunkLbPqControls:
    pass

class OutputSplunkLbQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputSplunkLbTLSSettingsClientSideMaximumTLSVersion(str, Enum):
    r"""Maximum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'

class OutputSplunkLbTLSSettingsClientSideMinimumTLSVersion(str, Enum):
    r"""Minimum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputSplunkLbTLSSettingsClientSide:
    ca_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    certificate_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificateName'), 'exclude': lambda f: f is None }})
    r"""The name of the predefined certificate."""
    cert_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    disabled: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    max_version: Optional[OutputSplunkLbTLSSettingsClientSideMaximumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxVersion'), 'exclude': lambda f: f is None }})
    r"""Maximum TLS version to use when connecting"""
    min_version: Optional[OutputSplunkLbTLSSettingsClientSideMinimumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minVersion'), 'exclude': lambda f: f is None }})
    r"""Minimum TLS version to use when connecting"""
    passphrase: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('passphrase'), 'exclude': lambda f: f is None }})
    r"""Passphrase to use to decrypt private key."""
    priv_key_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privKeyPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""
    


class OutputSplunkLbType(str, Enum):
    SPLUNK_LB = 'splunk_lb'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputSplunkLb:
    hosts: list[OutputSplunkLbHosts] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hosts') }})
    r"""Set of Splunk indexers to load-balance data to."""
    type: OutputSplunkLbType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    auth_token: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authToken'), 'exclude': lambda f: f is None }})
    r"""Shared secret token to use when establishing a connection to a Splunk indexer."""
    auth_type: Optional[OutputSplunkLbAuthenticationMethod] = dataclasses.field(default=OutputSplunkLbAuthenticationMethod.MANUAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""Enter a token directly, or provide a secret referencing a token"""
    connection_timeout: Optional[int] = dataclasses.field(default=10000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for the connection to establish before retrying"""
    dns_resolve_period_sec: Optional[int] = dataclasses.field(default=600, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dnsResolvePeriodSec'), 'exclude': lambda f: f is None }})
    r"""Re-resolve any hostnames every this many seconds and pick up destinations from A records."""
    enable_ack: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableACK'), 'exclude': lambda f: f is None }})
    r"""Check if indexer is shutting down and stop sending data. This helps minimize data loss during shutdown."""
    enable_multi_metrics: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableMultiMetrics'), 'exclude': lambda f: f is None }})
    r"""Output metrics in multiple-metric format in a single event. Supported in Splunk 8.0 and above."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    exclude_self: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeSelf'), 'exclude': lambda f: f is None }})
    r"""Exclude all IPs of the current host from the list of any resolved hostnames."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    indexer_discovery: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexerDiscovery'), 'exclude': lambda f: f is None }})
    r"""Automatically discover indexers in indexer clustering environment."""
    indexer_discovery_configs: Optional[OutputSplunkLbIndexerDiscoveryConfigs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexerDiscoveryConfigs'), 'exclude': lambda f: f is None }})
    r"""List of configurations to set up indexer discovery in Splunk Indexer clustering environment."""
    load_balance_stats_period_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loadBalanceStatsPeriodSec'), 'exclude': lambda f: f is None }})
    r"""How far back in time to keep traffic stats for load balancing purposes."""
    max_concurrent_senders: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxConcurrentSenders'), 'exclude': lambda f: f is None }})
    r"""Maximum number of concurrent connections (per worker process). A random set of IPs will be picked on every DNS resolution period. Use 0 for unlimited."""
    max_failed_health_checks: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFailedHealthChecks'), 'exclude': lambda f: f is None }})
    r"""Maximum number of times healthcheck can fail before we close connection. If set to 0 (disabled), and the connection to Splunk is forcibly closed, some data loss might occur."""
    max_s2_sversion: Optional[OutputSplunkLbMaxS2SVersion] = dataclasses.field(default=OutputSplunkLbMaxS2SVersion.V3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxS2Sversion'), 'exclude': lambda f: f is None }})
    r"""The highest S2S protocol version to advertise during handshake."""
    nested_fields: Optional[OutputSplunkLbNestedFieldSerialization] = dataclasses.field(default=OutputSplunkLbNestedFieldSerialization.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nestedFields'), 'exclude': lambda f: f is None }})
    r"""Specifies how to serialize nested fields into index-time fields."""
    on_backpressure: Optional[OutputSplunkLbBackpressureBehavior] = dataclasses.field(default=OutputSplunkLbBackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    optional_fields_in_general_section: Optional[OutputSplunkLbOptionalFieldsInGeneralSection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optionalFieldsInGeneralSection'), 'exclude': lambda f: f is None }})
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputSplunkLbCompression] = dataclasses.field(default=OutputSplunkLbCompression.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputSplunkLbPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default='1 MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputSplunkLbQueueFullBehavior] = dataclasses.field(default=OutputSplunkLbQueueFullBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/queues', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    sender_unhealthy_time_allowance: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('senderUnhealthyTimeAllowance'), 'exclude': lambda f: f is None }})
    r"""How long (in milliseconds) each LB endpoint can report blocked before the Destination reports unhealthy, blocking the sender. (Grace period for fluctuations.) Use 0 to disable; max 1 minute."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    throttle_rate_per_sec: Optional[str] = dataclasses.field(default='0', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throttleRatePerSec'), 'exclude': lambda f: f is None }})
    r"""Rate (in bytes per second) to throttle while writing to an output. Also takes values with multiple-byte units, such as KB, MB, GB, etc. (E.g., 42 MB.) Default value of 0 specifies no throttling."""
    tls: Optional[OutputSplunkLbTLSSettingsClientSide] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    write_timeout: Optional[int] = dataclasses.field(default=60000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('writeTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for a write to complete before assuming connection is dead"""
    

