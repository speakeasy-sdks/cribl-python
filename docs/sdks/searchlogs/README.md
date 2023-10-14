# SearchLogs
(*search_logs*)

### Available Operations

* [get](#get) - Get search logs

## get

Get search logs

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.search_logs.get(id='female')

if res.search_logs is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.GetSearchLogsResponse](../../models/operations/getsearchlogsresponse.md)**

