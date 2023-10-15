# LiveData
(*live_data*)

### Available Operations

* [post](#post) - Capture live incoming data

## post

Capture live incoming data

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.CaptureParams(
    filter='Producer base',
    level=871119,
    max_events=520911,
)

res = s.live_data.post(req)

if res.live_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.CaptureParams](../../models/shared/captureparams.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostLiveDataResponse](../../models/operations/postlivedataresponse.md)**

