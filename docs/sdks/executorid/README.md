# executor_id

### Available Operations

* [get](#get) - Get Executor by ID

## get

Get Executor by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetExecutorIDRequest(
    id='c480d3f2-132a-4f03-902d-514f4cc6f18b',
)

res = s.executor_id.get(req)

if res.executors is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetExecutorIDRequest](../../models/operations/getexecutoridrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetExecutorIDResponse](../../models/operations/getexecutoridresponse.md)**

