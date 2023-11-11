# OutputSplunk


## Fields

| Field                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `auth_token`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Shared secret token to use when establishing a connection to a Splunk indexer.                                                                                                                                                                   |
| `auth_type`                                                                                                                                                                                                                                      | [Optional[components.OutputSplunkAuthenticationMethod]](../../models/components/outputsplunkauthenticationmethod.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                               | Enter a token directly, or provide a secret referencing a token                                                                                                                                                                                  |
| `connection_timeout`                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Amount of time (milliseconds) to wait for the connection to establish before retrying                                                                                                                                                            |
| `enable_ack`                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Check if indexer is shutting down and stop sending data. This helps minimize data loss during shutdown.                                                                                                                                          |
| `enable_multi_metrics`                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Output metrics in multiple-metric format in a single event. Supported in Splunk 8.0 and above.                                                                                                                                                   |
| `environment`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere.                                                                                                                                             |
| `host`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | The hostname of the receiver                                                                                                                                                                                                                     |
| `id`                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Unique ID for this output                                                                                                                                                                                                                        |
| `max_failed_health_checks`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Maximum number of times healthcheck can fail before we close connection. If set to 0 (disabled), and the connection to Splunk is forcibly closed, some data loss might occur.                                                                    |
| `max_s2_sversion`                                                                                                                                                                                                                                | [Optional[components.MaxS2SVersion]](../../models/components/maxs2sversion.md)                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                               | The highest S2S protocol version to advertise during handshake.                                                                                                                                                                                  |
| `nested_fields`                                                                                                                                                                                                                                  | [Optional[components.NestedFieldSerialization]](../../models/components/nestedfieldserialization.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                               | Specifies how to serialize nested fields into index-time fields.                                                                                                                                                                                 |
| `on_backpressure`                                                                                                                                                                                                                                | [Optional[components.OutputSplunkBackpressureBehavior]](../../models/components/outputsplunkbackpressurebehavior.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                               | Whether to block, drop, or queue events when all receivers are exerting backpressure.                                                                                                                                                            |
| `pipeline`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Pipeline to process data before sending out to this output.                                                                                                                                                                                      |
| `port`                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The port to connect to on the provided host                                                                                                                                                                                                      |
| `pq_compress`                                                                                                                                                                                                                                    | [Optional[components.OutputSplunkCompression]](../../models/components/outputsplunkcompression.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                               | Codec to use to compress the persisted data.                                                                                                                                                                                                     |
| `pq_controls`                                                                                                                                                                                                                                    | [Optional[components.OutputSplunkPqControls]](../../models/components/outputsplunkpqcontrols.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `pq_max_file_size`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.).                                                                                                                                           |
| `pq_max_size`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc.                                               |
| `pq_on_backpressure`                                                                                                                                                                                                                             | [Optional[components.OutputSplunkQueueFullBehavior]](../../models/components/outputsplunkqueuefullbehavior.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                               | Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged. |
| `pq_path`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>.                                                                                                                            |
| `pq_strict_ordering`                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out).                                                                                                   |
| `streamtags`                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                               | Add tags for filtering and grouping in @{product}.                                                                                                                                                                                               |
| `system_fields`                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                               | Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported.                                                                                                                                       |
| `text_secret`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Select (or create) a stored text secret                                                                                                                                                                                                          |
| `throttle_rate_per_sec`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Rate (in bytes per second) to throttle while writing to an output. Also takes values with multiple-byte units, such as KB, MB, GB, etc. (E.g., 42 MB.) Default value of 0 specifies no throttling.                                               |
| `tls`                                                                                                                                                                                                                                            | [Optional[components.OutputSplunkTLSSettingsClientSide]](../../models/components/outputsplunktlssettingsclientside.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `type`                                                                                                                                                                                                                                           | [Optional[components.OutputSplunkType]](../../models/components/outputsplunktype.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `write_timeout`                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Amount of time (milliseconds) to wait for a write to complete before assuming connection is dead                                                                                                                                                 |