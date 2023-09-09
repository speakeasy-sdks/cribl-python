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


res = s.output_id.delete(id='molestiae')

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


res = s.output_id.get(id='delectus')

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


res = s.output_id.update(id='cupiditate', request_body=shared.OutputTcpjson(
    auth_token='numquam',
    auth_type=shared.OutputTcpjsonAuthenticationMethod.SECRET,
    compression=shared.OutputTcpjsonCompression.NONE,
    connection_timeout=873557,
    dns_resolve_period_sec=637856,
    environment='dignissimos',
    exclude_self=False,
    host='optio',
    hosts=[
        shared.OutputTcpjsonHosts(
            host='necessitatibus',
            port=359111,
            servername='qui',
            tls=shared.OutputTcpjsonHostsTLS.OFF,
            weight=532669,
        ),
    ],
    id='95c537c6-454e-4fb0-b348-96c3ca5acfbe',
    load_balance_stats_period_sec=141506,
    load_balanced=False,
    max_concurrent_senders=997437,
    on_backpressure=shared.OutputTcpjsonBackpressureBehavior.BLOCK,
    optional_fields_in_general_section=shared.OutputTcpjsonOptionalFieldsInGeneralSection.LOAD_BALANCED,
    pipeline='reprehenderit',
    port=45234,
    pq_compress=shared.OutputTcpjsonCompression.NONE,
    pq_controls=shared.OutputTcpjsonPqControls(),
    pq_max_file_size='minima',
    pq_max_size='in',
    pq_on_backpressure=shared.OutputTcpjsonQueueFullBehavior.BLOCK,
    pq_path='excepturi',
    pq_strict_ordering=False,
    streamtags=[
        'dolores',
    ],
    system_fields=[
        'error',
    ],
    text_secret='veritatis',
    throttle_rate_per_sec='ducimus',
    tls=shared.OutputTcpjsonTLSSettingsClientSide(
        ca_path='voluptate',
        cert_path='pariatur',
        certificate_name='itaque',
        disabled=False,
        max_version=shared.OutputTcpjsonTLSSettingsClientSideMaximumTLSVersion.TL_SV1_2,
        min_version=shared.OutputTcpjsonTLSSettingsClientSideMinimumTLSVersion.TL_SV1_3,
        passphrase='ex',
        priv_key_path='quaerat',
        reject_unauthorized=False,
        servername='commodi',
    ),
    token_ttl_minutes=888616,
    type=shared.OutputTcpjsonType.TCPJSON,
    write_timeout=810839,
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

