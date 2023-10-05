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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetLogFilesContentsRequest(
    et=700347,
    files='program',
    filter='Kia Cambridgeshire',
    group_id='payment withdrawal Car',
    limit=284160,
    lt=438142,
    type='Gasoline Cambridgeshire',
)

res = s.log_files_content.get(req)

if res.log_file_contents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetLogFilesContentsRequest](../../models/operations/getlogfilescontentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetLogFilesContentsResponse](../../models/operations/getlogfilescontentsresponse.md)**

