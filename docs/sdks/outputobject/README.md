# output_object

### Available Operations

* [create](#create) - Create Output

## create

Create Output

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.OutputSns(
    assume_role_arn='exercitationem',
    assume_role_external_id='quam',
    aws_api_key='dolorem',
    aws_authentication_method=shared.OutputSnsAuthenticationMethod.SECRET,
    aws_secret='ipsa',
    aws_secret_key='sint',
    enable_assume_role=False,
    endpoint='vero',
    environment='sequi',
    id='eb1e5a2b-12eb-407f-916d-b99545fc95fa',
    max_retries=559774,
    message_group_id='totam',
    on_backpressure=shared.OutputSnsBackpressureBehavior.DROP,
    pipeline='odio',
    pq_compress=shared.OutputSnsCompression.NONE,
    pq_controls=shared.OutputSnsPqControls(),
    pq_max_file_size='saepe',
    pq_max_size='architecto',
    pq_on_backpressure=shared.OutputSnsQueueFullBehavior.DROP,
    pq_path='iste',
    pq_strict_ordering=False,
    region=shared.OutputSnsRegion.ME_SOUTH_1,
    reject_unauthorized=False,
    reuse_connections=False,
    signature_version=shared.OutputSnsSignatureVersion.V4,
    streamtags=[
        'libero',
    ],
    system_fields=[
        'velit',
    ],
    topic_arn='doloremque',
    type=shared.OutputSnsType.SNS,
)

res = s.output_object.create(req)

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateOutputObjectResponse](../../models/operations/createoutputobjectresponse.md)**

