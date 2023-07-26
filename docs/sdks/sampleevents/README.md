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
            "aliquam": 'repudiandae',
            "amet": 'natus',
            "ab": 'officiis',
        },
        {
            "rerum": 'placeat',
            "ab": 'ad',
        },
        {
            "porro": 'labore',
            "impedit": 'ut',
            "earum": 'ullam',
        },
        {
            "enim": 'cupiditate',
            "occaecati": 'itaque',
        },
    ],
    input_id='fuga',
    level=234845,
    memory=268749,
    mode=shared.PreviewDataParamsMode.PIPE,
    pipeline_id='explicabo',
    sample_id='suscipit',
    sample_pipeline_id='ipsa',
    timeout=910410,
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

