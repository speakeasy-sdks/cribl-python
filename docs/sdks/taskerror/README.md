# task_error

### Available Operations

* [get](#get) - Get Task errors for a job by id

## get

Get Task errors for a job by id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetTaskErrorRequest(
    id='e4e080aa-1041-486e-8759-e02f3702c5c8',
)

res = s.task_error.get(req)

if res.task_errors is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetTaskErrorRequest](../../models/operations/gettaskerrorrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetTaskErrorResponse](../../models/operations/gettaskerrorresponse.md)**

