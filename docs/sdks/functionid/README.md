# function_id

### Available Operations

* [get](#get) - Get Function by ID

## get

Get Function by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetFunctionIDRequest(
    id='75d2367f-e1a0-4cc8-9f79-f0a396d90c36',
)

res = s.function_id.get(req)

if res.functions is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetFunctionIDRequest](../../models/operations/getfunctionidrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetFunctionIDResponse](../../models/operations/getfunctionidresponse.md)**

