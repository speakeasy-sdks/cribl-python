# condition

### Available Operations

* [get](#get) - Get Condition by ID

## get

Get Condition by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetConditionRequest(
    id='e7e253b6-6845-41c6-86e2-05e16deab3fe',
)

res = s.condition.get(req)

if res.conditions is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetConditionRequest](../../models/operations/getconditionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetConditionResponse](../../models/operations/getconditionresponse.md)**

