# cluis

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

req = operations.GetCluisRequest(
    context='nemo',
    query='asperiores',
)

res = s.cluis.get(req)

if res.clui_items is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetCluisRequest](../../models/operations/getcluisrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetCluisResponse](../../models/operations/getcluisresponse.md)**

