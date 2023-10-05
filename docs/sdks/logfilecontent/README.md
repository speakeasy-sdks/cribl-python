# LogFileContent
(*log_file_content*)

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

req = operations.GetLogFileContentRequest(
    end_offset=700347,
    et=90065,
    filter='Hatchback Kia',
    id='<ID>',
    limit=78592,
    lt=969961,
)

res = s.log_file_content.get(req)

if res.log_file_contents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetLogFileContentRequest](../../models/operations/getlogfilecontentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetLogFileContentResponse](../../models/operations/getlogfilecontentresponse.md)**

