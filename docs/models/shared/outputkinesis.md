# OutputKinesis


## Fields

| Field                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `assume_role_arn`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Amazon Resource Name (ARN) of the role to assume                                                                                                                                                                                                 |
| `assume_role_external_id`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | External ID to use when assuming role                                                                                                                                                                                                            |
| `aws_api_key`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Access key                                                                                                                                                                                                                                       |
| `aws_authentication_method`                                                                                                                                                                                                                      | [Optional[OutputKinesisAuthenticationMethod]](../../models/shared/outputkinesisauthenticationmethod.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                               | AWS authentication method. Choose Auto to use IAM roles.                                                                                                                                                                                         |
| `aws_secret`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Select (or create) a stored secret that references your access key and secret key.                                                                                                                                                               |
| `aws_secret_key`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Secret key                                                                                                                                                                                                                                       |
| `concurrency`                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Maximum number of ongoing put requests before blocking.                                                                                                                                                                                          |
| `enable_assume_role`                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Use Assume Role credentials to access Kinesis stream                                                                                                                                                                                             |
| `endpoint`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Kinesis stream service endpoint. If empty, defaults to AWS' Region-specific endpoint. Otherwise, it must point to Kinesis stream-compatible endpoint.                                                                                            |
| `environment`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere.                                                                                                                                             |
| `flush_period_sec`                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Maximum time between requests. Small values could cause the payload size to be smaller than the configured Max record size.                                                                                                                      |
| `id`                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Unique ID for this output                                                                                                                                                                                                                        |
| `max_record_size_kb`                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Maximum size (KB) of each individual record before compression. For non-compressible data 1MB is the max recommended size                                                                                                                        |
| `on_backpressure`                                                                                                                                                                                                                                | [Optional[OutputKinesisBackpressureBehavior]](../../models/shared/outputkinesisbackpressurebehavior.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                               | Whether to block, drop, or queue events when all receivers are exerting backpressure.                                                                                                                                                            |
| `pipeline`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Pipeline to process data before sending out to this output.                                                                                                                                                                                      |
| `pq_compress`                                                                                                                                                                                                                                    | [Optional[OutputKinesisCompression]](../../models/shared/outputkinesiscompression.md)                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                               | Codec to use to compress the persisted data.                                                                                                                                                                                                     |
| `pq_controls`                                                                                                                                                                                                                                    | [Optional[OutputKinesisPqControls]](../../models/shared/outputkinesispqcontrols.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `pq_max_file_size`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.).                                                                                                                                           |
| `pq_max_size`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc.                                               |
| `pq_on_backpressure`                                                                                                                                                                                                                             | [Optional[OutputKinesisQueueFullBehavior]](../../models/shared/outputkinesisqueuefullbehavior.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                               | Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged. |
| `pq_path`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>.                                                                                                                            |
| `pq_strict_ordering`                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out).                                                                                                   |
| `region`                                                                                                                                                                                                                                         | [OutputKinesisRegion](../../models/shared/outputkinesisregion.md)                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                               | Region where the Kinesis stream is located                                                                                                                                                                                                       |
| `reject_unauthorized`                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Whether to reject certificates that cannot be verified against a valid CA (e.g., self-signed certificates).                                                                                                                                      |
| `reuse_connections`                                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Whether to reuse connections between requests, which can improve performance.                                                                                                                                                                    |
| `signature_version`                                                                                                                                                                                                                              | [Optional[OutputKinesisSignatureVersion]](../../models/shared/outputkinesissignatureversion.md)                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Signature version to use for signing Kinesis stream requests.                                                                                                                                                                                    |
| `stream_name`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | Kinesis stream name to send events to.                                                                                                                                                                                                           |
| `streamtags`                                                                                                                                                                                                                                     | list[*str*]                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                               | Add tags for filtering and grouping in @{product}.                                                                                                                                                                                               |
| `system_fields`                                                                                                                                                                                                                                  | list[*str*]                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                               | Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported.                                                                                                                                       |
| `type`                                                                                                                                                                                                                                           | [Optional[OutputKinesisType]](../../models/shared/outputkinesistype.md)                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |