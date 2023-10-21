"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional

class OutputS3AuthenticationMethod(str, Enum):
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputS3Compress(str, Enum):
    r"""Choose data compression format to apply before moving files to final destination."""
    NONE = 'none'
    GZIP = 'gzip'

class OutputS3DataFormat(str, Enum):
    r"""Format of the output data."""
    PARQUET = 'parquet'
    RAW = 'raw'
    JSON = 'json'

class OutputS3ObjectACL(str, Enum):
    r"""Object ACL to assign to uploaded objects."""
    PRIVATE = 'private'
    PUBLIC_READ = 'public-read'
    PUBLIC_READ_WRITE = 'public-read-write'
    AUTHENTICATED_READ = 'authenticated-read'
    AWS_EXEC_READ = 'aws-exec-read'
    BUCKET_OWNER_READ = 'bucket-owner-read'
    BUCKET_OWNER_FULL_CONTROL = 'bucket-owner-full-control'

class OutputS3BackpressureBehavior(str, Enum):
    r"""Whether to block or drop events when all receivers are exerting backpressure."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputS3DataPageVersion(str, Enum):
    r"""Serialization format of data pages. Note that not all reader implentations support Data page V2."""
    DATA_PAGE_V1 = 'DATA_PAGE_V1'
    DATA_PAGE_V2 = 'DATA_PAGE_V2'

class OutputS3ParquetVersion(str, Enum):
    r"""Determines which data types are supported and how they are represented."""
    PARQUET_1_0 = 'PARQUET_1_0'
    PARQUET_2_4 = 'PARQUET_2_4'
    PARQUET_2_6 = 'PARQUET_2_6'

class OutputS3Region(str, Enum):
    r"""Region where the S3 bucket is located."""
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

class OutputS3ServerSideEncryption(str, Enum):
    r"""Server-side encryption for uploaded objects."""
    AWS_KMS = 'aws:kms'

class OutputS3SignatureVersion(str, Enum):
    r"""Signature version to use for signing S3 requests."""
    V2 = 'v2'
    V4 = 'v4'

class OutputS3StorageClass(str, Enum):
    r"""Storage class to select for uploaded objects."""
    STANDARD = 'STANDARD'
    REDUCED_REDUNDANCY = 'REDUCED_REDUNDANCY'
    STANDARD_IA = 'STANDARD_IA'
    ONEZONE_IA = 'ONEZONE_IA'
    INTELLIGENT_TIERING = 'INTELLIGENT_TIERING'
    GLACIER = 'GLACIER'
    DEEP_ARCHIVE = 'DEEP_ARCHIVE'

class OutputS3Type(str, Enum):
    S3 = 's3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OutputS3:
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    r"""Name of the destination S3 bucket. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. E.g., referencing a Global Variable: `myBucket-${C.vars.myVar}`."""
    dest_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destPath') }})
    r"""Prefix to append to files before uploading. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. E.g., referencing a Global Variable: `myKeyPrefix-${C.vars.myVar}`."""
    add_id_to_stage_path: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addIdToStagePath'), 'exclude': lambda f: f is None }})
    r"""Append output's ID to staging location."""
    assume_role_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assumeRoleArn'), 'exclude': lambda f: f is None }})
    r"""Amazon Resource Name (ARN) of the role to assume"""
    assume_role_external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assumeRoleExternalId'), 'exclude': lambda f: f is None }})
    r"""External ID to use when assuming role"""
    aws_api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsApiKey'), 'exclude': lambda f: f is None }})
    r"""Access key. This value can be a constant or a JavaScript expression(e.g., `${C.env.SOME_ACCESS_KEY}`)."""
    aws_authentication_method: Optional[OutputS3AuthenticationMethod] = dataclasses.field(default=OutputS3AuthenticationMethod.undefined, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsAuthenticationMethod'), 'exclude': lambda f: f is None }})
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    aws_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored secret that references your access key and secret key."""
    aws_secret_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsSecretKey'), 'exclude': lambda f: f is None }})
    r"""Secret key. This value can be a constant or a JavaScript expression(e.g., `${C.env.SOME_SECRET}`)."""
    base_file_name: Optional[str] = dataclasses.field(default='`CriblOut`', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseFileName'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to define the output filename prefix (can be constant)."""
    compress: Optional[OutputS3Compress] = dataclasses.field(default=OutputS3Compress.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Choose data compression format to apply before moving files to final destination."""
    empty_dir_cleanup_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emptyDirCleanupSec'), 'exclude': lambda f: f is None }})
    r"""How often (secs) to clean-up empty directories when 'Remove Staging Dirs' is enabled."""
    enable_assume_role: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableAssumeRole'), 'exclude': lambda f: f is None }})
    r"""Use Assume Role credentials to access S3"""
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""S3 service endpoint. If empty, defaults to AWS' Region-specific endpoint. Otherwise, it must point to S3-compatible endpoint."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    file_name_suffix: Optional[str] = dataclasses.field(default='`.${C.env["CRIBL_WORKER_ID"]}.${__format}${__compression === "gzip" ? ".gz" : ""}`', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileNameSuffix'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to define the output filename suffix (can be constant).  The `__format` variable refers to the value of the `Data format` field (`json` or `raw`).  The `__compression` field refers to the kind of compression being used (`none` or `gzip`)"""
    format: Optional[OutputS3DataFormat] = dataclasses.field(default=OutputS3DataFormat.JSON, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Format of the output data."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    kms_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kmsKeyId'), 'exclude': lambda f: f is None }})
    r"""ID or ARN of the KMS customer-managed key to use for encryption"""
    max_concurrent_file_parts: Optional[int] = dataclasses.field(default=4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxConcurrentFileParts'), 'exclude': lambda f: f is None }})
    r"""Maximum number of parts to upload in parallel per file. Minimum part size is 5MB."""
    max_file_idle_time_sec: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFileIdleTimeSec'), 'exclude': lambda f: f is None }})
    r"""Maximum amount of time to keep inactive files open. Files open for longer than this will be closed and moved to final output location."""
    max_file_open_time_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFileOpenTimeSec'), 'exclude': lambda f: f is None }})
    r"""Maximum amount of time to write to a file. Files open for longer than this will be closed and moved to final output location."""
    max_file_size_mb: Optional[int] = dataclasses.field(default=32, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFileSizeMB'), 'exclude': lambda f: f is None }})
    r"""Maximum uncompressed output file size. Files of this size will be closed and moved to final output location."""
    max_open_files: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxOpenFiles'), 'exclude': lambda f: f is None }})
    r"""Maximum number of files to keep open concurrently. When exceeded, @{product} will close the oldest open files and move them to the final output location."""
    object_acl: Optional[OutputS3ObjectACL] = dataclasses.field(default=OutputS3ObjectACL.PRIVATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('objectACL'), 'exclude': lambda f: f is None }})
    r"""Object ACL to assign to uploaded objects."""
    on_backpressure: Optional[OutputS3BackpressureBehavior] = dataclasses.field(default=OutputS3BackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when all receivers are exerting backpressure."""
    parquet_data_page_version: Optional[OutputS3DataPageVersion] = dataclasses.field(default=OutputS3DataPageVersion.DATA_PAGE_V1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetDataPageVersion'), 'exclude': lambda f: f is None }})
    r"""Serialization format of data pages. Note that not all reader implentations support Data page V2."""
    parquet_page_size: Optional[str] = dataclasses.field(default='1MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetPageSize'), 'exclude': lambda f: f is None }})
    r"""Ideal memory size for page segments. E.g., 1MB or 128MB. Generally, lower values improve reading speed, while higher values improve compression. Imposes a target, not a strict limit; the final size of a row group may be larger or smaller."""
    parquet_row_group_size: Optional[str] = dataclasses.field(default='16MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetRowGroupSize'), 'exclude': lambda f: f is None }})
    r"""Ideal memory size for row group segments. E.g., 128MB or 1GB. Affects memory use when writing. Imposes a target, not a strict limit; the final size of a row group may be larger or smaller."""
    parquet_version: Optional[OutputS3ParquetVersion] = dataclasses.field(default=OutputS3ParquetVersion.PARQUET_2_6, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetVersion'), 'exclude': lambda f: f is None }})
    r"""Determines which data types are supported and how they are represented."""
    partition_expr: Optional[str] = dataclasses.field(default='C.Time.strftime(_time ? _time : Date.now()/1000, \'%Y/%m/%d\')', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partitionExpr'), 'exclude': lambda f: f is None }})
    r"""JS expression defining how files are partitioned and organized. Default is date-based. If blank, Stream will fall back to the event's __partition field value – if present – otherwise to each location's root directory."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    region: Optional[OutputS3Region] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Region where the S3 bucket is located."""
    reject_unauthorized: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejectUnauthorized'), 'exclude': lambda f: f is None }})
    r"""Whether to reject certificates that cannot be verified against a valid CA (e.g., self-signed certificates)."""
    remove_empty_dirs: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removeEmptyDirs'), 'exclude': lambda f: f is None }})
    r"""Remove empty staging directories after moving files."""
    reuse_connections: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reuseConnections'), 'exclude': lambda f: f is None }})
    r"""Whether to reuse connections between requests, which can improve performance."""
    server_side_encryption: Optional[OutputS3ServerSideEncryption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serverSideEncryption'), 'exclude': lambda f: f is None }})
    r"""Server-side encryption for uploaded objects."""
    should_log_invalid_rows: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shouldLogInvalidRows'), 'exclude': lambda f: f is None }})
    r"""To log rows that @{product} skips due to data mismatch, first set logging to Debug, then toggle this on. Logs up to 20 unique rows."""
    signature_version: Optional[OutputS3SignatureVersion] = dataclasses.field(default=OutputS3SignatureVersion.V4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signatureVersion'), 'exclude': lambda f: f is None }})
    r"""Signature version to use for signing S3 requests."""
    spacer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spacer'), 'exclude': lambda f: f is None }})
    stage_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/outputs/staging', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stagePath'), 'exclude': lambda f: f is None }})
    r"""Filesystem location in which to buffer files, before compressing and moving to final destination. Use performant stable storage."""
    storage_class: Optional[OutputS3StorageClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storageClass'), 'exclude': lambda f: f is None }})
    r"""Storage class to select for uploaded objects."""
    streamtags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    type: Optional[OutputS3Type] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

