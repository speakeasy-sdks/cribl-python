# SampleEvents
(*sample_events*)

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
            "nostrum": 'molestiae',
        },
    ],
    input_id='veniam',
    level=969206,
    memory=66207,
    mode=shared.PreviewDataParamsMode.PIPE,
    pipeline_id='aut',
    sample_id='aut',
    sample_pipeline_id='eveniet',
    timeout=483753,
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

