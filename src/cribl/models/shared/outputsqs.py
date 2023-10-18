"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional

class OutputSqsAuthenticationMethod(str, Enum):
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputSqsBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputSqsCompression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'


@dataclasses.dataclass
class OutputSqsPqControls:
    pass

class OutputSqsQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputSqsQueueType(str, Enum):
    r"""The queue type used (or created). Defaults to Standard."""
    STANDARD = 'standard'
    FIFO = 'fifo'

class OutputSqsRegion(str, Enum):
    r"""AWS Region where the SQS queue is located. Required, unless the Queue entry is a URL or ARN that includes a Region."""
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

class OutputSqsSignatureVersion(str, Enum):
    r"""Signature version to use for signing SQS requests."""
    V2 = 'v2'
    V4 = 'v4'

class OutputSqsType(str, Enum):
    SQS = 'sqs'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputSqs:
    queue_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queueName') }})
    r"""The name, URL, or ARN of the SQS queue to send events to. When a non-AWS URL is specified, format must be: '{url}/myQueueName'. E.g., 'https://host:port/myQueueName'. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. E.g., referencing a Global Variable: `https://host:port/myQueue-${C.vars.myVar}`."""
    assume_role_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assumeRoleArn'), 'exclude': lambda f: f is None }})
    r"""Amazon Resource Name (ARN) of the role to assume"""
    assume_role_external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assumeRoleExternalId'), 'exclude': lambda f: f is None }})
    r"""External ID to use when assuming role"""
    aws_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsAccountId'), 'exclude': lambda f: f is None }})
    r"""SQS queue owner's AWS account ID. Leave empty if SQS queue is in same AWS account."""
    aws_api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsApiKey'), 'exclude': lambda f: f is None }})
    r"""Access key"""
    aws_authentication_method: Optional[OutputSqsAuthenticationMethod] = dataclasses.field(default=OutputSqsAuthenticationMethod.undefined, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsAuthenticationMethod'), 'exclude': lambda f: f is None }})
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    aws_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored secret that references your access key and secret key."""
    aws_secret_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsSecretKey'), 'exclude': lambda f: f is None }})
    r"""Secret key"""
    create_queue: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createQueue'), 'exclude': lambda f: f is None }})
    r"""Create queue if it does not exist."""
    enable_assume_role: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableAssumeRole'), 'exclude': lambda f: f is None }})
    r"""Use Assume Role credentials to access SQS"""
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""SQS service endpoint. If empty, defaults to AWS' Region-specific endpoint. Otherwise, it must point to SQS-compatible endpoint."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    flush_period_sec: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max record size."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    max_in_progress: Optional[int] = dataclasses.field(default=10, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxInProgress'), 'exclude': lambda f: f is None }})
    r"""The maximum number of in-progress API requests before backpressure is applied."""
    max_queue_size: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxQueueSize'), 'exclude': lambda f: f is None }})
    r"""Maximum number of queued batches before blocking."""
    max_record_size_kb: Optional[int] = dataclasses.field(default=256, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxRecordSizeKB'), 'exclude': lambda f: f is None }})
    r"""Maximum size (KB) of batches to send. Per the SQS spec, the max allowed value is 256 KB."""
    message_group_id: Optional[str] = dataclasses.field(default='cribl', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messageGroupId'), 'exclude': lambda f: f is None }})
    r"""This parameter applies only to FIFO queues. The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner. Use event field __messageGroupId to override this value."""
    on_backpressure: Optional[OutputSqsBackpressureBehavior] = dataclasses.field(default=OutputSqsBackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    pq_compress: Optional[OutputSqsCompression] = dataclasses.field(default=OutputSqsCompression.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputSqsPqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default='1 MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputSqsQueueFullBehavior] = dataclasses.field(default=OutputSqsQueueFullBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/queues', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    queue_type: Optional[OutputSqsQueueType] = dataclasses.field(default=OutputSqsQueueType.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queueType'), 'exclude': lambda f: f is None }})
    r"""The queue type used (or created). Defaults to Standard."""
    region: Optional[OutputSqsRegion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""AWS Region where the SQS queue is located. Required, unless the Queue entry is a URL or ARN that includes a Region."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Whether to reject certificates that cannot be verified against a valid CA (e.g., self-signed certificates)."""
    reuse_connections: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reuseConnections'), 'exclude': lambda f: f is None }})
    r"""Whether to reuse connections between requests, which can improve performance."""
    signature_version: Optional[OutputSqsSignatureVersion] = dataclasses.field(default=OutputSqsSignatureVersion.V4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signatureVersion'), 'exclude': lambda f: f is None }})
    r"""Signature version to use for signing SQS requests."""
    streamtags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    type: Optional[OutputSqsType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

