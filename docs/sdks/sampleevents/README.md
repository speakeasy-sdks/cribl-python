# SampleEvents

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
            "natus": 'provident',
        },
    ],
    input_id='cum',
    level=983854,
    memory=703966,
    mode=shared.PreviewDataParamsMode.ROUTE_AND_SEND,
    pipeline_id='itaque',
    sample_id='laboriosam',
    sample_pipeline_id='unde',
    timeout=263767,
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

