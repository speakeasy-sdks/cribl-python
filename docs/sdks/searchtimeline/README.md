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


res = s.search_timeline.get(id='magnam')

if res.search_timeline is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.GetSearchTimelineResponse](../../models/operations/getsearchtimelineresponse.md)**

