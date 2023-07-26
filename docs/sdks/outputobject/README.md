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

req = shared.OutputLoki(
    auth_type=shared.OutputLokiAuthenticationType.CREDENTIALS_SECRET,
    compress=False,
    concurrency=617238,
    credentials_secret='repellendus',
    environment='voluptates',
    extra_http_headers=[
        shared.OutputLokiExtraHTTPHeaders(
            name='Ms. Nicolas Kuphal',
            value='tempore',
        ),
    ],
    failed_request_logging_mode=shared.OutputLokiFailedRequestLoggingMode.PAYLOAD_AND_HEADERS,
    flush_period_sec=846427,
    id='a08c57fa-6c78-4a21-ae19-bafeca619149',
    labels=[
        shared.OutputLokiLabels(
            name='Megan Baumbach',
            value='eius',
        ),
        shared.OutputLokiLabels(
            name='Toby Lubowitz',
            value='ab',
        ),
        shared.OutputLokiLabels(
            name='Jennifer Waters I',
            value='distinctio',
        ),
    ],
    max_payload_events=312563,
    max_payload_size_kb=955358,
    message='neque',
    message_format=shared.OutputLokiMessageFormat.PROTOBUF,
    on_backpressure=shared.OutputLokiBackpressureBehavior.BLOCK,
    password='numquam',
    pipeline='mollitia',
    pq_compress=shared.OutputLokiCompression.GZIP,
    pq_controls=shared.OutputLokiPqControls(),
    pq_max_file_size='blanditiis',
    pq_max_size='suscipit',
    pq_on_backpressure=shared.OutputLokiQueueFullBehavior.DROP,
    pq_path='quis',
    pq_strict_ordering=False,
    reject_unauthorized=False,
    safe_headers=[
        'corporis',
        'iste',
    ],
    streamtags=[
        'autem',
        'voluptate',
    ],
    system_fields=[
        'magni',
    ],
    text_secret='animi',
    timeout_sec=676274,
    token='voluptas',
    type=shared.OutputLokiType.LOKI,
    url='temporibus',
    use_round_robin_dns=False,
    username='Ozella.Rice',
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

