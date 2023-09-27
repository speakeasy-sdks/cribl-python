# LogFileList
(*log_file_list*)

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


res = s.log_file_list.get(allow='maiores', depth=967260, mode='vel', path='architecto')

if res.edge_files is not None:
    # handle response
```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `allow`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | query array[string] optional List of allowed-filename wildcard patterns |
| `depth`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Search depth for "manual" mode                                          |
| `mode`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Discovery Mode (default is "auto")                                      |
| `path`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Search directory for "manual" mode                                      |


### Response

**[operations.GetLogFileListResponse](../../models/operations/getlogfilelistresponse.md)**

