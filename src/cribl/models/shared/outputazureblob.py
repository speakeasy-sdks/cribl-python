"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class OutputAzureBlobAuthenticationMethod(str, Enum):
    r"""Enter connection string directly, or select a stored secret"""
    SECRET = 'secret'
    MANUAL = 'manual'

class OutputAzureBlobCompress(str, Enum):
    r"""Choose data compression format to apply before moving files to final destination."""
    NONE = 'none'
    GZIP = 'gzip'

class OutputAzureBlobDataFormat(str, Enum):
    r"""Format of the output data."""
    PARQUET = 'parquet'
    RAW = 'raw'
    JSON = 'json'

class OutputAzureBlobBackpressureBehavior(str, Enum):
    r"""Whether to block or drop events when all receivers are exerting backpressure."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputAzureBlobDataPageVersion(str, Enum):
    r"""Serialization format of data pages. Note that not all reader implentations support Data page V2."""
    DATA_PAGE_V1 = 'DATA_PAGE_V1'
    DATA_PAGE_V2 = 'DATA_PAGE_V2'

class OutputAzureBlobParquetVersion(str, Enum):
    r"""Determines which data types are supported and how they are represented."""
    PARQUET_1_0 = 'PARQUET_1_0'
    PARQUET_2_4 = 'PARQUET_2_4'
    PARQUET_2_6 = 'PARQUET_2_6'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputAzureBlob:
    container_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('containerName') }})
    r"""A container organizes a set of blobs, similar to a directory in a file system. Value can be a JavaScript expression enclosed in quotes or backticks. @{product} evaluates the expression at init time. The expression can evaluate to a constant value, and can reference Global Variables, e.g., `myContainer-${C.env[\\"CRIBL_WORKER_ID\\"]}`"""
    dest_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destPath') }})
    r"""Root directory prepended to path before uploading. Value can be a JavaScript expression enclosed in quotes or backticks. @{product} evaluates the expression at init time. The expression can evaluate to a constant value, and can reference Global Variables, e.g., `myBlobPrefix-${C.env[\\"CRIBL_WORKER_ID\\"]}`"""
    add_id_to_stage_path: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addIdToStagePath'), 'exclude': lambda f: f is None }})
    r"""Append output's ID to staging location."""
    auth_type: Optional[OutputAzureBlobAuthenticationMethod] = dataclasses.field(default=OutputAzureBlobAuthenticationMethod.MANUAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType'), 'exclude': lambda f: f is None }})
    r"""Enter connection string directly, or select a stored secret"""
    base_file_name: Optional[str] = dataclasses.field(default='`CriblOut`', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseFileName'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to define the output filename prefix (can be constant)."""
    compress: Optional[OutputAzureBlobCompress] = dataclasses.field(default=OutputAzureBlobCompress.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compress'), 'exclude': lambda f: f is None }})
    r"""Choose data compression format to apply before moving files to final destination."""
    connection_string: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionString'), 'exclude': lambda f: f is None }})
    r"""Enter your Azure Storage account connection string. If left blank, Stream will fall back to env.AZURE_STORAGE_CONNECTION_STRING."""
    create_container: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createContainer'), 'exclude': lambda f: f is None }})
    r"""Creates the configured container in Azure Blob Storage if it does not already exist."""
    empty_dir_cleanup_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emptyDirCleanupSec'), 'exclude': lambda f: f is None }})
    r"""How often (secs) to clean-up empty directories when 'Remove Staging Dirs' is enabled."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    file_name_suffix: Optional[str] = dataclasses.field(default='`.${C.env["CRIBL_WORKER_ID"]}.${__format}${__compression === "gzip" ? ".gz" : ""}`', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileNameSuffix'), 'exclude': lambda f: f is None }})
    r"""JavaScript expression to define the output filename suffix (can be constant).  The `__format` variable refers to the value of the `Data format` field (`json` or `raw`).  The `__compression` field refers to the kind of compression being used (`none` or `gzip`)"""
    format: Optional[OutputAzureBlobDataFormat] = dataclasses.field(default=OutputAzureBlobDataFormat.JSON, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Format of the output data."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    max_file_idle_time_sec: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFileIdleTimeSec'), 'exclude': lambda f: f is None }})
    r"""Maximum amount of time to keep inactive files open. Files open for longer than this will be closed and moved to final output location."""
    max_file_open_time_sec: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFileOpenTimeSec'), 'exclude': lambda f: f is None }})
    r"""Maximum amount of time to write to a file. Files open for longer than this will be closed and moved to final output location."""
    max_file_size_mb: Optional[int] = dataclasses.field(default=32, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxFileSizeMB'), 'exclude': lambda f: f is None }})
    r"""Maximum uncompressed output file size. Files of this size will be closed and moved to final output location."""
    max_open_files: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxOpenFiles'), 'exclude': lambda f: f is None }})
    r"""Maximum number of files to keep open concurrently. When exceeded, @{product} will close the oldest open files and move them to the final output location."""
    on_backpressure: Optional[OutputAzureBlobBackpressureBehavior] = dataclasses.field(default=OutputAzureBlobBackpressureBehavior.BLOCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when all receivers are exerting backpressure."""
    parquet_data_page_version: Optional[OutputAzureBlobDataPageVersion] = dataclasses.field(default=OutputAzureBlobDataPageVersion.DATA_PAGE_V1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetDataPageVersion'), 'exclude': lambda f: f is None }})
    r"""Serialization format of data pages. Note that not all reader implentations support Data page V2."""
    parquet_page_size: Optional[str] = dataclasses.field(default='1MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetPageSize'), 'exclude': lambda f: f is None }})
    r"""Ideal memory size for page segments. E.g., 1MB or 128MB. Generally, lower values improve reading speed, while higher values improve compression. Imposes a target, not a strict limit; the final size of a row group may be larger or smaller."""
    parquet_row_group_size: Optional[str] = dataclasses.field(default='16MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetRowGroupSize'), 'exclude': lambda f: f is None }})
    r"""Ideal memory size for row group segments. E.g., 128MB or 1GB. Affects memory use when writing. Imposes a target, not a strict limit; the final size of a row group may be larger or smaller."""
    parquet_version: Optional[OutputAzureBlobParquetVersion] = dataclasses.field(default=OutputAzureBlobParquetVersion.PARQUET_2_6, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parquetVersion'), 'exclude': lambda f: f is None }})
    r"""Determines which data types are supported and how they are represented."""
    partition_expr: Optional[str] = dataclasses.field(default='C.Time.strftime(_time ? _time : Date.now()/1000, \'%Y/%m/%d\')', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partitionExpr'), 'exclude': lambda f: f is None }})
    r"""JS expression defining how files are partitioned and organized. Default is date-based. If blank, Stream will fall back to the event's __partition field value – if present – otherwise to each location's root directory."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    remove_empty_dirs: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removeEmptyDirs'), 'exclude': lambda f: f is None }})
    r"""Remove empty staging directories after moving files."""
    should_log_invalid_rows: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shouldLogInvalidRows'), 'exclude': lambda f: f is None }})
    r"""To log rows that @{product} skips due to data mismatch, first set logging to Debug, then toggle this on. Logs up to 20 unique rows."""
    spacer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spacer'), 'exclude': lambda f: f is None }})
    stage_path: Optional[str] = dataclasses.field(default='$CRIBL_HOME/state/outputs/staging', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stagePath'), 'exclude': lambda f: f is None }})
    r"""Filesystem location in which to buffer files, before compressing and moving to final destination. Use performant stable storage."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    text_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textSecret'), 'exclude': lambda f: f is None }})
    r"""Select (or create) a stored text secret"""
    TYPE: Final[Optional[str]] = dataclasses.field(default='azure_blob', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

