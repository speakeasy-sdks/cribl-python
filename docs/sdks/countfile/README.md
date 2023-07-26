# count_file

### Available Operations

* [get](#get) - get the count of files of changed

## get

get the count of files of changed

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetCountFileRequest(
    group='expedita',
)

res = s.count_file.get(req)

if res.count_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetCountFileRequest](../../models/operations/getcountfilerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetCountFileResponse](../../models/operations/getcountfileresponse.md)**

