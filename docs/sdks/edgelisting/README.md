# EdgeListing
(*.edge_listing*)

### Available Operations

* [get](#get) - Get a directory listing of the given path

## get

Get a directory listing of the given path

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.edge_listing.get(path='string')

if res.filesystem_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `path`             | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetEdgeListingResponse](../../models/operations/getedgelistingresponse.md)**

