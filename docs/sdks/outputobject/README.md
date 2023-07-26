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

req = shared.OutputAzureLogs(
    api_url='eveniet',
    auth_type=shared.OutputAzureLogsAuthenticationMethod.MANUAL,
    compress=False,
    concurrency=150349,
    environment='impedit',
    extra_http_headers=[
        shared.OutputAzureLogsExtraHTTPHeaders(
            name='Duane Romaguera',
            value='beatae',
        ),
        shared.OutputAzureLogsExtraHTTPHeaders(
            name='Ebony Waters',
            value='illo',
        ),
        shared.OutputAzureLogsExtraHTTPHeaders(
            name='Cody Schiller',
            value='cum',
        ),
    ],
    failed_request_logging_mode=shared.OutputAzureLogsFailedRequestLoggingMode.PAYLOAD_AND_HEADERS,
    flush_period_sec=906495,
    id='ec74378b-a253-4177-87dc-915ad2caf5dd',
    keypair_secret='commodi',
    log_type='esse',
    max_payload_events=127499,
    max_payload_size_kb=233708,
    on_backpressure=shared.OutputAzureLogsBackpressureBehavior.BLOCK,
    pipeline='optio',
    pq_compress=shared.OutputAzureLogsCompression.NONE,
    pq_controls=shared.OutputAzureLogsPqControls(),
    pq_max_file_size='maiores',
    pq_max_size='exercitationem',
    pq_on_backpressure=shared.OutputAzureLogsQueueFullBehavior.DROP,
    pq_path='repudiandae',
    pq_strict_ordering=False,
    reject_unauthorized=False,
    resource_id='aspernatur',
    safe_headers=[
        'neque',
        'officia',
        'suscipit',
        'harum',
    ],
    streamtags=[
        'doloremque',
        'perferendis',
    ],
    system_fields=[
        'iusto',
        'corrupti',
        'molestiae',
    ],
    timeout_sec=340101,
    type=shared.OutputAzureLogsType.AZURE_LOGS,
    use_round_robin_dns=False,
    workspace_id='iure',
    workspace_key='ab',
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

