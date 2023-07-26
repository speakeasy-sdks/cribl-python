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
    filter='odio',
    level=616941,
    max_events=588152,
    step_duration=739508,
    worker_id='doloribus',
    worker_threshold=703966,
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

