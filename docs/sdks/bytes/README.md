# bytes

### Available Operations

* [get](#get) - Get some number of bytes from the file at the given path

## get

Get some number of bytes from the file at the given path

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetBytesRequest(
    bytes_requested=715208,
    path='voluptatum',
)

res = s.bytes.get(req)

if res.sample_files is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetBytesRequest](../../models/operations/getbytesrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetBytesResponse](../../models/operations/getbytesresponse.md)**

