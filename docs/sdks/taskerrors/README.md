# task_errors

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

req = operations.GetTaskErrorsRequest(
    group='recusandae',
    id='2d30ead3-104f-4a44-b07b-f375b4428282',
)

res = s.task_errors.get(req)

if res.task_errors is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetTaskErrorsRequest](../../models/operations/gettaskerrorsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetTaskErrorsResponse](../../models/operations/gettaskerrorsresponse.md)**

