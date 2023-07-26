# changed_files

### Available Operations

* [get](#get) - get the files changed

## get

get the files changed

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetChangedFilesRequest(
    id='6c645b08-b618-491b-aa0f-e1ade008e6f8',
    group='minus',
)

res = s.changed_files.get(req)

if res.changed_files is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetChangedFilesRequest](../../models/operations/getchangedfilesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetChangedFilesResponse](../../models/operations/getchangedfilesresponse.md)**

