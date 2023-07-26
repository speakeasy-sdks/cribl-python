# search_logs

### Available Operations

* [get](#get) - Get search logs

## get

Get search logs

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSearchLogsRequest(
    id='4ba9f78a-5c0e-4d7a-ab62-e97261fb0c58',
)

res = s.search_logs.get(req)

if res.search_logs is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetSearchLogsRequest](../../models/operations/getsearchlogsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetSearchLogsResponse](../../models/operations/getsearchlogsresponse.md)**

