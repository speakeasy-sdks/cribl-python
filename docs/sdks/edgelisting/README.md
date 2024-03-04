# EdgeListing
(*edge_listing*)

### Available Operations

* [get](#get) - Get a directory listing of the given path

## get

Get a directory listing of the given path

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.edge_listing.get(path='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
