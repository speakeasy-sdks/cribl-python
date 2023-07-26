# edge_listing

### Available Operations

* [get](#get) - Get a directory listing of the given path

## get

Get a directory listing of the given path

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetEdgeListingRequest(
    path='quasi',
)

res = s.edge_listing.get(req)

if res.filesystem_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetEdgeListingRequest](../../models/operations/getedgelistingrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetEdgeListingResponse](../../models/operations/getedgelistingresponse.md)**

