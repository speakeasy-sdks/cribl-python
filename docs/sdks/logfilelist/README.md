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
    bearer_auth="",
)


res = s.log_file_list.get(allow='string', depth=700347, mode='string', path='string')

if res.edge_files is not None:
    # handle response
    pass
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

