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

req = operations.DeleteOutputIDRequest(
    id='cf79da18-a782-42bf-9589-4e6861adb55f',
)

res = s.output_id.delete(req)

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteOutputIDRequest](../../models/operations/deleteoutputidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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

req = operations.GetOutputIDRequest(
    id='9e5d751c-9fe8-4f75-82bf-dc3450841f17',
)

res = s.output_id.get(req)

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetOutputIDRequest](../../models/operations/getoutputidrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


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

req = operations.UpdateOutputIDRequest(
    request_body=shared.OutputKafka(
        ack=shared.OutputKafkaAcknowledgments.ONE,
        authentication_timeout=261219,
        brokers=[
            'ex',
            'amet',
        ],
        compression=shared.OutputKafkaCompression.GZIP,
        connection_timeout=565304,
        environment='voluptatibus',
        flush_event_count=217167,
        flush_period_sec=944260,
        format=shared.OutputKafkaRecordDataFormat.RAW,
        id='27e21f86-2657-4b36-bc6b-9f587ce525c6',
        kafka_schema_registry=shared.OutputKafkaKafkaSchemaRegistryAuthentication(
            default_key_schema_id=462136,
            default_value_schema_id=410916,
            disabled=False,
            schema_registry_url='numquam',
            tls=shared.OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSide(
                ca_path='architecto',
                cert_path='fuga',
                certificate_name='totam',
                disabled=False,
                max_version=shared.OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMaximumTLSVersion.TL_SV1,
                min_version=shared.OutputKafkaKafkaSchemaRegistryAuthenticationTLSSettingsClientSideMinimumTLSVersion.TL_SV1,
                passphrase='sed',
                priv_key_path='officiis',
                reject_unauthorized=False,
                servername='veniam',
            ),
        ),
        max_record_size_kb=61844,
        max_retries=292883,
        on_backpressure=shared.OutputKafkaBackpressureBehavior.DROP,
        pipeline='libero',
        pq_compress=shared.OutputKafkaCompression1.NONE,
        pq_controls=shared.OutputKafkaPqControls(),
        pq_max_file_size='cumque',
        pq_max_size='quia',
        pq_on_backpressure=shared.OutputKafkaQueueFullBehavior.BLOCK,
        pq_path='porro',
        pq_strict_ordering=False,
        reauthentication_threshold=767880,
        request_timeout=714933,
        sasl=shared.OutputKafkaAuthentication(
            disabled=False,
            mechanism=shared.OutputKafkaAuthenticationSASLMechanism.SCRAM_SHA_256,
        ),
        streamtags=[
            'amet',
        ],
        system_fields=[
            'facilis',
            'minus',
            'vero',
        ],
        tls=shared.OutputKafkaTLSSettingsClientSide(
            ca_path='impedit',
            cert_path='omnis',
            certificate_name='et',
            disabled=False,
            max_version=shared.OutputKafkaTLSSettingsClientSideMaximumTLSVersion.TL_SV1_3,
            min_version=shared.OutputKafkaTLSSettingsClientSideMinimumTLSVersion.TL_SV1_2,
            passphrase='est',
            priv_key_path='distinctio',
            reject_unauthorized=False,
            servername='fugiat',
        ),
        topic='nulla',
        type=shared.OutputKafkaType.KAFKA,
    ),
    id='88e71f6c-4825-42d7-b71e-7fd074009ef8',
)

res = s.output_id.update(req)

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateOutputIDRequest](../../models/operations/updateoutputidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateOutputIDResponse](../../models/operations/updateoutputidresponse.md)**

