"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class OutputKafkaAcknowledgments(int, Enum):
    r"""Control the number of required acknowledgments."""
    ONE = 1
    ZERO = 0
    MINUS_1 = -1

class OutputKafkaCompression(str, Enum):
    r"""Codec to use to compress the data before sending to Kafka"""
    NONE = 'none'
    GZIP = 'gzip'
    SNAPPY = 'snappy'
    LZ4 = 'lz4'

class OutputKafkaRecordDataFormat(str, Enum):
    r"""Format to use to serialize events before writing to Kafka."""
    JSON = 'json'
    RAW = 'raw'

class OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMaximumTLSVersion(str, Enum):
    r"""Maximum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'

class OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMinimumTLSVersion(str, Enum):
    r"""Minimum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSide:
    ca_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    certificate_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificateName'), 'exclude': lambda f: f is None }})
    r"""The name of the predefined certificate."""
    cert_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    max_version: Optional[OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMaximumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxVersion'), 'exclude': lambda f: f is None }})
    r"""Maximum TLS version to use when connecting"""
    min_version: Optional[OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMinimumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minVersion'), 'exclude': lambda f: f is None }})
    r"""Minimum TLS version to use when connecting"""
    passphrase: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('passphrase'), 'exclude': lambda f: f is None }})
    r"""Passphrase to use to decrypt private key."""
    priv_key_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privKeyPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputKafkaKafkaSchemaRegistryAuthentication:
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    r"""Enable Schema Registry"""
    default_key_schema_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultKeySchemaId'), 'exclude': lambda f: f is None }})
    r"""Used when __keySchemaIdOut is not present, to transform key values, leave blank if key transformation is not required by default."""
    default_value_schema_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultValueSchemaId'), 'exclude': lambda f: f is None }})
    r"""Used when __valueSchemaIdOut is not present, to transform _raw, leave blank if value transformation is not required by default."""
    schema_registry_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemaRegistryURL'), 'exclude': lambda f: f is None }})
    r"""URL for access to the Confluent Schema Registry, i.e.: http://localhost:8081"""
    tls: Optional[OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSide] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    


class OutputKafkaBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputKafkaCompression1(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class OutputKafkaPqControls:
    pass

class OutputKafkaQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputKafkaAuthenticationSASLMechanism(str, Enum):
    r"""SASL authentication mechanism to use."""
    PLAIN = 'plain'
    SCRAM_SHA_256 = 'scram-sha-256'
    SCRAM_SHA_512 = 'scram-sha-512'
    KERBEROS = 'kerberos'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputKafkaAuthentication:
    r"""Authentication parameters to use when connecting to brokers. Using TLS is highly recommended."""
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    r"""Enable Authentication"""
    mechanism: Optional[OutputKafkaAuthenticationSASLMechanism] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mechanism'), 'exclude': lambda f: f is None }})
    r"""SASL authentication mechanism to use."""
    


class OutputKafkaTLSSettingsClientSideMaximumTLSVersion(str, Enum):
    r"""Maximum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'

class OutputKafkaTLSSettingsClientSideMinimumTLSVersion(str, Enum):
    r"""Minimum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputKafkaTLSSettingsClientSide:
    ca_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    certificate_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificateName'), 'exclude': lambda f: f is None }})
    r"""The name of the predefined certificate."""
    cert_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    max_version: Optional[OutputKafkaTLSSettingsClientSideMaximumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxVersion'), 'exclude': lambda f: f is None }})
    r"""Maximum TLS version to use when connecting"""
    min_version: Optional[OutputKafkaTLSSettingsClientSideMinimumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minVersion'), 'exclude': lambda f: f is None }})
    r"""Minimum TLS version to use when connecting"""
    passphrase: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('passphrase'), 'exclude': lambda f: f is None }})
    r"""Passphrase to use to decrypt private key."""
    priv_key_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privKeyPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""
    


class OutputKafkaType(str, Enum):
    KAFKA = 'kafka'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputKafka:
    brokers: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brokers') }})
    r"""Enter each Kafka broker you want to use. Specify hostname and port, e.g., mykafkabroker:9092, or just hostname, in which case @{product} will assign port 9092."""
    topic: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic') }})
    r"""The topic to publish events to. Can be overridden using the __topicOut field."""
    ack: Optional[OutputKafkaAcknowledgments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ack'), 'exclude': lambda f: f is None }})
    r"""Control the number of required acknowledgments."""
    authentication_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authenticationTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time to wait for Kafka to respond to an authentication request"""
    compression: Optional[OutputKafkaCompression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the data before sending to Kafka"""
    connection_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time to wait for a connection to complete successfully"""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    flush_event_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushEventCount'), 'exclude': lambda f: f is None }})
    r"""The maximum number of events you want the Destination to allow in a batch before forcing a flush"""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of time you want the Destination to wait before forcing a flush. Shorter intervals tend to result in smaller batches being sent."""
    format: Optional[OutputKafkaRecordDataFormat] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Format to use to serialize events before writing to Kafka."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    kafka_schema_registry: Optional[OutputKafkaKafkaSchemaRegistryAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kafkaSchemaRegistry'), 'exclude': lambda f: f is None }})
    max_record_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxRecordSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size of each record batch before compression. The value must not exceed the Kafka brokers' message.max.bytes setting."""
    max_retries: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxRetries'), 'exclude': lambda f: f is None }})
    r"""If messages are failing, you can set the maximum number of retries as high as 100 to prevent loss of data."""
    on_backpressure: Optional[OutputKafkaBackpressureBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputKafkaCompression1] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputKafkaPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputKafkaQueueFullBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    reauthentication_threshold: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reauthenticationThreshold'), 'exclude': lambda f: f is None }})
    r"""Specifies a time window during which @{product} can reauthenticate if needed. Creates the window measuring backwards from the moment when credentials are set to expire."""
    request_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time to wait for Kafka to respond to a request"""
    sasl: Optional[OutputKafkaAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sasl'), 'exclude': lambda f: f is None }})
    r"""Authentication parameters to use when connecting to brokers. Using TLS is highly recommended."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    tls: Optional[OutputKafkaTLSSettingsClientSide] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    type: Optional[OutputKafkaType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

