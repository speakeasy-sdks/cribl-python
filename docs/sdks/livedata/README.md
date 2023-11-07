# LiveData
(*.live_data*)

### Available Operations

* [post](#post) - Capture live incoming data

## post

Capture live incoming data

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.CaptureParams(
    filter='string',
    level=449035,
    max_events=690234,
)

res = s.live_data.post(req)

if res.live_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.CaptureParams](../../models/shared/captureparams.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.PostLiveDataResponse](../../models/operations/postlivedataresponse.md)**

