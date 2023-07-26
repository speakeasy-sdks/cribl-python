# search_timeline

### Available Operations

* [get](#get) - Get search timeline

## get

Get search timeline

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSearchTimelineRequest(
    id='d27b5199-6b5b-44b5-8eef-712b7a7ab034',
)

res = s.search_timeline.get(req)

if res.search_timeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetSearchTimelineRequest](../../models/operations/getsearchtimelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetSearchTimelineResponse](../../models/operations/getsearchtimelineresponse.md)**

