# LogFileContent
(*.log_file_content*)

### Available Operations

* [get](#get) - Get contents of the log file

## get

Get contents of the log file

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)

req = operations.GetLogFileContentRequest(
    id='<ID>',
)

res = s.log_file_content.get(req)

if res.log_file_contents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetLogFileContentRequest](../../models/operations/getlogfilecontentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetLogFileContentResponse](../../models/operations/getlogfilecontentresponse.md)**

