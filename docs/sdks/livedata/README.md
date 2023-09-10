# live_data

### Available Operations

* [post](#post) - Capture live incoming data

## post

Capture live incoming data

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.CaptureParams(
    filter='fugit',
    level=764995,
    max_events=684935,
    step_duration=189062,
    worker_id='animi',
    worker_threshold=898760,
)

res = s.live_data.post(req)

if res.live_data is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.CaptureParams](../../models/shared/captureparams.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostLiveDataResponse](../../models/operations/postlivedataresponse.md)**

