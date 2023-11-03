# FunctionID
(*function_id*)

### Available Operations

* [get](#get) - Get Function by ID

## get

Get Function by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.function_id.get(id='string')

if res.functions is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetFunctionIDResponse](../../models/operations/getfunctionidresponse.md)**

