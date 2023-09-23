# OutputID

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


res = s.output_id.delete(id='nostrum')

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


res = s.output_id.get(id='omnis')

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


res = s.output_id.update(id='libero', request_body=shared.OutputSplunkLb(
    auth_token='id',
    auth_type=shared.OutputSplunkLbAuthenticationMethod.MANUAL,
    connection_timeout=854460,
    dns_resolve_period_sec=637462,
    enable_ack=False,
    enable_multi_metrics=False,
    environment='quos',
    exclude_self=False,
    hosts=[
        shared.OutputSplunkLbHosts(
            host='placeat',
            port=25756,
            servername='iusto',
            tls=shared.OutputSplunkLbHostsTLS.INHERIT,
            weight=914864,
        ),
    ],
    id='1084cb06-72d1-4ad8-b9ee-b9665b85efbd',
    indexer_discovery=False,
    indexer_discovery_configs=shared.OutputSplunkLbIndexerDiscoveryConfigs(
        auth_token='alias',
        auth_type=shared.OutputSplunkLbIndexerDiscoveryConfigsAuthenticationMethod.SECRET,
        master_uri='quidem',
        refresh_interval_sec=684126,
        site='repudiandae',
        text_secret='accusantium',
    ),
    load_balance_stats_period_sec=710456,
    max_concurrent_senders=885208,
    max_failed_health_checks=177005,
    max_s2_sversion=shared.OutputSplunkLbMaxS2SVersion.V4,
    nested_fields=shared.OutputSplunkLbNestedFieldSerialization.JSON,
    on_backpressure=shared.OutputSplunkLbBackpressureBehavior.DROP,
    optional_fields_in_general_section=shared.OutputSplunkLbOptionalFieldsInGeneralSection.INDEXER_DISCOVERY,
    pipeline='explicabo',
    pq_compress=shared.OutputSplunkLbCompression.NONE,
    pq_controls=shared.OutputSplunkLbPqControls(),
    pq_max_file_size='error',
    pq_max_size='earum',
    pq_on_backpressure=shared.OutputSplunkLbQueueFullBehavior.BLOCK,
    pq_path='recusandae',
    pq_strict_ordering=False,
    sender_unhealthy_time_allowance=630871,
    streamtags=[
        'ut',
    ],
    system_fields=[
        'quidem',
    ],
    text_secret='quis',
    throttle_rate_per_sec='beatae',
    tls=shared.OutputSplunkLbTLSSettingsClientSide(
        ca_path='unde',
        cert_path='molestiae',
        certificate_name='delectus',
        disabled=False,
        max_version=shared.OutputSplunkLbTLSSettingsClientSideMaximumTLSVersion.TL_SV1_2,
        min_version=shared.OutputSplunkLbTLSSettingsClientSideMinimumTLSVersion.TL_SV1,
        passphrase='numquam',
        priv_key_path='numquam',
        reject_unauthorized=False,
        servername='nesciunt',
    ),
    type=shared.OutputSplunkLbType.SPLUNK_LB,
    write_timeout=873557,
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

