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
    bearer_auth="",
)

req = shared.PreviewDataParams(
    events=[
        {
            "payment": 'Silver',
        },
    ],
    mode=shared.PreviewDataParamsMode.ROUTE,
    pipeline_id='Transexual',
    sample_id='protocol',
)

res = s.sample_events.post(req)

if res.live_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.PreviewDataParams](../../models/shared/previewdataparams.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostSampleEventsResponse](../../models/operations/postsampleeventsresponse.md)**

