# SavedQuery
(*.saved_query*)

### Available Operations

* [get](#get) - Get SavedQuery by ID

## get

Get SavedQuery by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_query.get(id='string')

if res.saved_query is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetSavedQueryResponse](../../models/operations/getsavedqueryresponse.md)**

