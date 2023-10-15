# LogFilesContent
(*log_files_content*)

### Available Operations

* [get](#get) - Get contents of the log file

## get

Get contents of the log file

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)

req = operations.GetLogFilesContentsRequest(
    type='Northeast Hatchback Kia',
)

res = s.log_files_content.get(req)

if res.log_file_contents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetLogFilesContentsRequest](../../models/operations/getlogfilescontentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetLogFilesContentsResponse](../../models/operations/getlogfilescontentsresponse.md)**

