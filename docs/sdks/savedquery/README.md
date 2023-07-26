# saved_query

### Available Operations

* [get](#get) - Get SavedQuery by ID

## get

Get SavedQuery by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSavedQueryRequest(
    id='185472f9-ee69-4166-a8be-3444eac8b3a2',
)

res = s.saved_query.get(req)

if res.saved_query is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetSavedQueryRequest](../../models/operations/getsavedqueryrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetSavedQueryResponse](../../models/operations/getsavedqueryresponse.md)**

