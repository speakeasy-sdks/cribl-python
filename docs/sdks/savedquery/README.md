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


res = s.saved_query.get(id='excepturi')

if res.saved_query is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetSavedQueryResponse](../../models/operations/getsavedqueryresponse.md)**

