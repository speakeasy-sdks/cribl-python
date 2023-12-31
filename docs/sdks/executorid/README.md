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


res = s.executor_id.get('ad')

if res.executors is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetExecutorIDResponse](../../models/operations/getexecutoridresponse.md)**

