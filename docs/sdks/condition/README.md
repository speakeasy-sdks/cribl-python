# Condition
(*condition*)

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


res = s.condition.get(id='female')

if res.conditions is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetConditionResponse](../../models/operations/getconditionresponse.md)**

