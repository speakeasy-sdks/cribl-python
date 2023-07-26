# log_file_list

### Available Operations

* [get](#get) - list log files

## get

list log files

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetLogFileListRequest(
    allow='reiciendis',
    depth=170934,
    mode='dolore',
    path='pariatur',
)

res = s.log_file_list.get(req)

if res.edge_files is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetLogFileListRequest](../../models/operations/getlogfilelistrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetLogFileListResponse](../../models/operations/getlogfilelistresponse.md)**

