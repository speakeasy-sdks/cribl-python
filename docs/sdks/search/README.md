# Search

### Available Operations

* [dispatch_search](#dispatch_search) - Dispatch search *id* to worker nodes filtered by worker node filter using RPC

## dispatch_search

Dispatch search *id* to worker nodes filtered by worker node filter using RPC

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.search.dispatch_search(id='veniam')

if res.search_id is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.DispatchSearchResponse](../../models/operations/dispatchsearchresponse.md)**

