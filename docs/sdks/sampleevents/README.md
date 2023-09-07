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
            "facere": 'impedit',
        },
    ],
    input_id='quasi',
    level=647218,
    memory=801075,
    mode=shared.PreviewDataParamsMode.ROUTE,
    pipeline_id='doloremque',
    sample_id='voluptatem',
    sample_pipeline_id='facere',
    timeout=901008,
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

