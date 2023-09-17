# LogFileContents

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

req = operations.GetLogFileContentsRequest(
    end_offset=671384,
    et=123844,
    filter='nostrum',
    group_id='fugiat',
    id='b6a66065-9a1a-4dea-ab58-51d6c645b08b',
    limit=399660,
    lt=109784,
    offset=530860,
)

res = s.log_file_contents.get(req)

if res.log_file_contents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetLogFileContentsRequest](../../models/operations/getlogfilecontentsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetLogFileContentsResponse](../../models/operations/getlogfilecontentsresponse.md)**

