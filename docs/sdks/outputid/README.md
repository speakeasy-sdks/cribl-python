# output_id

### Available Operations

* [delete](#delete) - Delete Output
* [get](#get) - Get Output by ID
* [update](#update) - Update Output

## delete

Delete Output

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.output_id.delete(id='voluptatum')

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteOutputIDResponse](../../models/operations/deleteoutputidresponse.md)**


## get

Get Output by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.output_id.get(id='iusto')

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetOutputIDResponse](../../models/operations/getoutputidresponse.md)**


## update

Update Output

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.output_id.update(id='quod', request_body=shared.OutputDlS3(
    add_id_to_stage_path=False,
    assume_role_arn='voluptas',
    assume_role_external_id='non',
    aws_api_key='ullam',
    aws_authentication_method=shared.OutputDlS3AuthenticationMethod.MANUAL,
    aws_secret='voluptas',
    aws_secret_key='doloribus',
    base_file_name='animi',
    bucket='recusandae',
    compress=shared.OutputDlS3Compress.NONE,
    dest_path='non',
    empty_dir_cleanup_sec=900368,
    enable_assume_role=False,
    endpoint='distinctio',
    environment='maiores',
    file_name_suffix='laboriosam',
    format=shared.OutputDlS3DataFormat.PARQUET,
    id='c321f023-b75d-4236-bfe1-a0cc8df79f0a',
    kms_key_id='nesciunt',
    max_concurrent_file_parts=590998,
    max_file_idle_time_sec=404774,
    max_file_open_time_sec=832944,
    max_file_size_mb=601277,
    max_open_files=1116,
    object_acl=shared.OutputDlS3ObjectACL.BUCKET_OWNER_READ,
    on_backpressure=shared.OutputDlS3BackpressureBehavior.BLOCK,
    parquet_data_page_version=shared.OutputDlS3DataPageVersion.DATA_PAGE_V1,
    parquet_page_size='labore',
    parquet_row_group_size='expedita',
    parquet_version=shared.OutputDlS3ParquetVersion.PARQUET_2_4,
    partition_expr='quisquam',
    partitioning_fields=[
        'enim',
    ],
    pipeline='nulla',
    region=shared.OutputDlS3Region.US_GOV_WEST_1,
    reject_unauthorized=False,
    remove_empty_dirs=False,
    reuse_connections=False,
    server_side_encryption=shared.OutputDlS3ServerSideEncryption.AWS_KMS,
    should_log_invalid_rows=False,
    signature_version=shared.OutputDlS3SignatureVersion.V4,
    spacer='mollitia',
    stage_path='impedit',
    storage_class=shared.OutputDlS3StorageClass.DEEP_ARCHIVE,
    streamtags=[
        'quas',
    ],
    system_fields=[
        'cum',
        'dicta',
        'impedit',
    ],
    type=shared.OutputDlS3Type.DL_S3,
))

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `id`                        | *str*                       | :heavy_check_mark:          | Unique ID                   |
| `request_body`              | *Optional[Any]*             | :heavy_minus_sign:          | Output object to be updated |


### Response

**[operations.UpdateOutputIDResponse](../../models/operations/updateoutputidresponse.md)**

