"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional

class OutputTcpjsonAuthenticationMethod(str, Enum):
    r"""Enter a token directly, or provide a secret referencing a token"""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputTcpjsonCompression(str, Enum):
    r"""Codec to use to compress the data before sending"""
    NONE = 'none'
    GZIP = 'gzip'

class OutputTcpjsonHostsTLS(str, Enum):
    r"""Whether to inherit TLS configs from group setting or disable TLS."""
    INHERIT = 'inherit'
    OFF = 'off'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputTcpjsonHosts:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The hostname of the receiver."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""The port to connect to on the provided host."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Servername to use if establishing a TLS connection. If not specified, defaults to connection host (iff not an IP); otherwise, to the global TLS settings."""
    tls: Optional[OutputTcpjsonHostsTLS] = dataclasses.field(default=OutputTcpjsonHostsTLS.INHERIT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    r"""Whether to inherit TLS configs from group setting or disable TLS."""
    weight: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    r"""The weight to use for load-balancing purposes."""
    


class OutputTcpjsonBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputTcpjsonOptionalFieldsInGeneralSection(str, Enum):
    LOAD_BALANCED = 'loadBalanced'
    HOSTS = 'hosts'


@dataclasses.dataclass
class OutputTcpjsonPqControls:
    pass

class OutputTcpjsonQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputTcpjsonTLSSettingsClientSideMaximumTLSVersion(str, Enum):
    r"""Maximum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'

class OutputTcpjsonTLSSettingsClientSideMinimumTLSVersion(str, Enum):
    r"""Minimum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputTcpjsonTLSSettingsClientSide:
    ca_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    certificate_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificateName'), 'exclude': lambda f: f is None }})
    r"""The name of the predefined certificate."""
    cert_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    disabled: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    max_version: Optional[OutputTcpjsonTLSSettingsClientSideMaximumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxVersion'), 'exclude': lambda f: f is None }})
    r"""Maximum TLS version to use when connecting"""
    min_version: Optional[OutputTcpjsonTLSSettingsClientSideMinimumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minVersion'), 'exclude': lambda f: f is None }})
    r"""Minimum TLS version to use when connecting"""
    passphrase: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('passphrase'), 'exclude': lambda f: f is None }})
    r"""Passphrase to use to decrypt private key."""
    priv_key_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privKeyPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""
    


class OutputTcpjsonType(str, Enum):
    TCPJSON = 'tcpjson'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputTcpjson:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique ID for this output"""
    type: OutputTcpjsonType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    auth_token: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authToken'), 'exclude': lambda f: f is None }})
    r"""Optional authentication token to include as part of the connection header"""
    auth_type: Optional[OutputTcpjsonAuthenticationMethod] = dataclasses.field(default=OutputTcpjsonAuthenticationMethod.MANUAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""Enter a token directly, or provide a secret referencing a token"""
    compression: Optional[OutputTcpjsonCompression] = dataclasses.field(default=OutputTcpjsonCompression.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the data before sending"""
    connection_timeout: Optional[int] = dataclasses.field(default=10000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for the connection to establish before retrying"""
    dns_resolve_period_sec: Optional[int] = dataclasses.field(default=600, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dnsResolvePeriodSec'), 'exclude': lambda f: f is None }})
    r"""Re-resolve any hostnames every this many seconds and pick up destinations from A records."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    exclude_self: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeSelf'), 'exclude': lambda f: f is None }})
    r"""Exclude all IPs of the current host from the list of any resolved hostnames."""
    host: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host'), 'exclude': lambda f: f is None }})
    r"""The hostname of the receiver"""
    hosts: Optional[List[OutputTcpjsonHosts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hosts'), 'exclude': lambda f: f is None }})
    r"""Set of hosts to load-balance data to."""
    load_balanced: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loadBalanced'), 'exclude': lambda f: f is None }})
    r"""Use load-balanced destinations"""
    load_balance_stats_period_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loadBalanceStatsPeriodSec'), 'exclude': lambda f: f is None }})
    r"""How far back in time to keep traffic stats for load balancing purposes."""
    max_concurrent_senders: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxConcurrentSenders'), 'exclude': lambda f: f is None }})
    r"""Maximum number of concurrent connections (per worker process). A random set of IPs will be picked on every DNS resolution period. Use 0 for unlimited."""
    on_backpressure: Optional[OutputTcpjsonBackpressureBehavior] = dataclasses.field(default=OutputTcpjsonBackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    optional_fields_in_general_section: Optional[OutputTcpjsonOptionalFieldsInGeneralSection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optionalFieldsInGeneralSection'), 'exclude': lambda f: f is None }})
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    port: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The port to connect to on the provided host"""
    pq_compress: Optional[OutputTcpjsonCompression] = dataclasses.field(default=OutputTcpjsonCompression.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputTcpjsonPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default='1 MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputTcpjsonQueueFullBehavior] = dataclasses.field(default=OutputTcpjsonQueueFullBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/queues', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    streamtags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    throttle_rate_per_sec: Optional[str] = dataclasses.field(default='0', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throttleRatePerSec'), 'exclude': lambda f: f is None }})
    r"""Rate (in bytes per second) to throttle while writing to an output. Also takes values with multiple-byte units, such as KB, MB, GB, etc. (E.g., 42 MB.) Default value of 0 specifies no throttling."""
    tls: Optional[OutputTcpjsonTLSSettingsClientSide] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    token_ttl_minutes: Optional[int] = dataclasses.field(default=60, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokenTTLMinutes'), 'exclude': lambda f: f is None }})
    r"""The number of minutes before the internally generated authentication token expires, valid values between 1 and 60"""
    write_timeout: Optional[int] = dataclasses.field(default=60000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('writeTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for a write to complete before assuming connection is dead"""
    

