# sample_events

### Available Operations

* [post](#post) - Sends sample events through a pipeline and returns the results

## post

Sends sample events through a pipeline and returns the results

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.PreviewDataParams(
    cpu_profile=False,
    dropped=False,
    events=[
        {
            "ipsam": 'eos',
        },
        {
            "minima": 'laudantium',
            "quibusdam": 'fuga',
        },
        {
            "excepturi": 'corporis',
            "nam": 'itaque',
            "suscipit": 'porro',
        },
        {
            "consequatur": 'qui',
            "in": 'enim',
            "vel": 'impedit',
            "consectetur": 'quis',
        },
    ],
    input_id='ut',
    level=668155,
    memory=682847,
    mode=shared.PreviewDataParamsMode.PIPE,
    pipeline_id='adipisci',
    sample_id='ratione',
    sample_pipeline_id='cum',
    timeout=300732,
)

res = s.sample_events.post(req)

if res.live_data is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.PreviewDataParams](../../models/shared/previewdataparams.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostSampleEventsResponse](../../models/operations/postsampleeventsresponse.md)**

