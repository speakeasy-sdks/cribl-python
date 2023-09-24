"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class OutputMskAcknowledgments(int, Enum):
    r"""Control the number of required acknowledgments."""
    ONE = 1
    ZERO = 0
    MINUS_1 = -1

class OutputMskAuthenticationMethod(str, Enum):
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputMskCompression(str, Enum):
    r"""Codec to use to compress the data before sending to Kafka"""
    NONE = 'none'
    GZIP = 'gzip'
    SNAPPY = 'snappy'
    LZ4 = 'lz4'

class OutputMskRecordDataFormat(str, Enum):
    r"""Format to use to serialize events before writing to Kafka."""
    JSON = 'json'
    RAW = 'raw'

class OutputMskKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMaximumTLSVersion(str, Enum):
    r"""Maximum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'

class OutputMskKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMinimumTLSVersion(str, Enum):
    r"""Minimum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputMskKafkaSchemaRegistryAuthenticationTLSSettingsClientSide:
    ca_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    certificate_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificateName'), 'exclude': lambda f: f is None }})
    r"""The name of the predefined certificate."""
    cert_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    max_version: Optional[OutputMskKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMaximumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxVersion'), 'exclude': lambda f: f is None }})
    r"""Maximum TLS version to use when connecting"""
    min_version: Optional[OutputMskKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMinimumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minVersion'), 'exclude': lambda f: f is None }})
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
class OutputMskKafkaSchemaRegistryAuthentication:
    default_key_schema_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultKeySchemaId'), 'exclude': lambda f: f is None }})
    r"""Used when __keySchemaIdOut is not present, to transform key values, leave blank if key transformation is not required by default."""
    default_value_schema_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultValueSchemaId'), 'exclude': lambda f: f is None }})
    r"""Used when __valueSchemaIdOut is not present, to transform _raw, leave blank if value transformation is not required by default."""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    r"""Enable Schema Registry"""
    schema_registry_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemaRegistryURL'), 'exclude': lambda f: f is None }})
    r"""URL for access to the Confluent Schema Registry, i.e.: http://localhost:8081"""
    tls: Optional[OutputMskKafkaSchemaRegistryAuthenticationTLSSettingsClientSide] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    


class OutputMskBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputMskCompression1(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class OutputMskPqControls:
    pass

class OutputMskQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputMskRegion(str, Enum):
    r"""Region where the MSK cluster is located"""
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'
    AF_SOUTH_1 = 'af-south-1'
    CA_CENTRAL_1 = 'ca-central-1'
    EU_WEST_1 = 'eu-west-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_WEST_2 = 'eu-west-2'
    EU_SOUTH_1 = 'eu-south-1'
    EU_WEST_3 = 'eu-west-3'
    EU_NORTH_1 = 'eu-north-1'
    AP_EAST_1 = 'ap-east-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    AP_SOUTH_1 = 'ap-south-1'
    ME_SOUTH_1 = 'me-south-1'
    SA_EAST_1 = 'sa-east-1'
    US_GOV_EAST_1 = 'us-gov-east-1'
    US_GOV_WEST_1 = 'us-gov-west-1'

class OutputMskSignatureVersion(str, Enum):
    r"""Signature version to use for signing MSK cluster requests."""
    V2 = 'v2'
    V4 = 'v4'

class OutputMskTLSSettingsClientSideMaximumTLSVersion(str, Enum):
    r"""Maximum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'

class OutputMskTLSSettingsClientSideMinimumTLSVersion(str, Enum):
    r"""Minimum TLS version to use when connecting"""
    TL_SV1 = 'TLSv1'
    TL_SV1_1 = 'TLSv1.1'
    TL_SV1_2 = 'TLSv1.2'
    TL_SV1_3 = 'TLSv1.3'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputMskTLSSettingsClientSide:
    ca_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    certificate_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificateName'), 'exclude': lambda f: f is None }})
    r"""The name of the predefined certificate."""
    cert_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    max_version: Optional[OutputMskTLSSettingsClientSideMaximumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxVersion'), 'exclude': lambda f: f is None }})
    r"""Maximum TLS version to use when connecting"""
    min_version: Optional[OutputMskTLSSettingsClientSideMinimumTLSVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minVersion'), 'exclude': lambda f: f is None }})
    r"""Minimum TLS version to use when connecting"""
    passphrase: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('passphrase'), 'exclude': lambda f: f is None }})
    r"""Passphrase to use to decrypt private key."""
    priv_key_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privKeyPath'), 'exclude': lambda f: f is None }})
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). Defaults to No."""
    servername: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servername'), 'exclude': lambda f: f is None }})
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""
    


class OutputMskType(str, Enum):
    MSK = 'msk'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputMsk:
    brokers: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brokers') }})
    r"""Enter each Kafka broker you want to use. Specify hostname and port, e.g., mykafkabroker:9092, or just hostname, in which case @{product} will assign port 9092."""
    region: OutputMskRegion = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""Region where the MSK cluster is located"""
    topic: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic') }})
    r"""The topic to publish events to. Can be overridden using the __topicOut field."""
    ack: Optional[OutputMskAcknowledgments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ack'), 'exclude': lambda f: f is None }})
    r"""Control the number of required acknowledgments."""
    assume_role_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assumeRoleArn'), 'exclude': lambda f: f is None }})
    r"""Amazon Resource Name (ARN) of the role to assume"""
    assume_role_external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assumeRoleExternalId'), 'exclude': lambda f: f is None }})
    r"""External ID to use when assuming role"""
    authentication_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authenticationTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time to wait for Kafka to respond to an authentication request"""
    aws_api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsApiKey'), 'exclude': lambda f: f is None }})
    r"""Access key"""
    aws_authentication_method: Optional[OutputMskAuthenticationMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsAuthenticationMethod'), 'exclude': lambda f: f is None }})
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    aws_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored secret that references your access key and secret key."""
    aws_secret_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsSecretKey'), 'exclude': lambda f: f is None }})
    r"""Secret key"""
    compression: Optional[OutputMskCompression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the data before sending to Kafka"""
    connection_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time to wait for a connection to complete successfully"""
    enable_assume_role: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableAssumeRole'), 'exclude': lambda f: f is None }})
    r"""Use Assume Role credentials to access MSK"""
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""MSK cluster service endpoint. If empty, defaults to AWS' Region-specific endpoint. Otherwise, it must point to MSK cluster-compatible endpoint."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    flush_event_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushEventCount'), 'exclude': lambda f: f is None }})
    r"""The maximum number of events you want the Destination to allow in a batch before forcing a flush"""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of time you want the Destination to wait before forcing a flush. Shorter intervals tend to result in smaller batches being sent."""
    format: Optional[OutputMskRecordDataFormat] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Format to use to serialize events before writing to Kafka."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    kafka_schema_registry: Optional[OutputMskKafkaSchemaRegistryAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kafkaSchemaRegistry'), 'exclude': lambda f: f is None }})
    max_record_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxRecordSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size of each record batch before compression. The value must not exceed the Kafka brokers' message.max.bytes setting."""
    max_retries: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxRetries'), 'exclude': lambda f: f is None }})
    r"""If messages are failing, you can set the maximum number of retries as high as 100 to prevent loss of data."""
    on_backpressure: Optional[OutputMskBackpressureBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputMskCompression1] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputMskPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputMskQueueFullBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    reauthentication_threshold: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reauthenticationThreshold'), 'exclude': lambda f: f is None }})
    r"""Specifies a time window during which @{product} can reauthenticate if needed. Creates the window measuring backwards from the moment when credentials are set to expire."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Whether to reject certificates that cannot be verified against a valid CA (e.g., self-signed certificates)."""
    request_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time to wait for Kafka to respond to a request"""
    reuse_connections: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reuseConnections'), 'exclude': lambda f: f is None }})
    r"""Whether to reuse connections between requests, which can improve performance."""
    signature_version: Optional[OutputMskSignatureVersion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signatureVersion'), 'exclude': lambda f: f is None }})
    r"""Signature version to use for signing MSK cluster requests."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    tls: Optional[OutputMskTLSSettingsClientSide] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tls'), 'exclude': lambda f: f is None }})
    type: Optional[OutputMskType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

