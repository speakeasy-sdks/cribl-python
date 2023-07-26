# search

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

req = operations.DispatchSearchRequest(
    id='643664a8-f0af-48c6-91d7-32d9fbaf9476',
)

res = s.search.dispatch_search(req)

if res.search_id is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DispatchSearchRequest](../../models/operations/dispatchsearchrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DispatchSearchResponse](../../models/operations/dispatchsearchresponse.md)**

