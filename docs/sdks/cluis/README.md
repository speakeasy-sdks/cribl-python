# Cluis
(*cluis*)

### Available Operations

* [get](#get) - Get CLUI search results

## get

Get CLUI search results

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.cluis.get(query='suscipit', context='deserunt')

if res.clui_items is not None:
    # handle response
```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `query`                                         | *str*                                           | :heavy_check_mark:                              | Search query                                    |
| `context`                                       | *Optional[str]*                                 | :heavy_minus_sign:                              | Search query context, either "stream" or "edge" |


### Response

**[operations.GetCluisResponse](../../models/operations/getcluisresponse.md)**

