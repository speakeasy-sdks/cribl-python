# LogFileContents
(*log_file_contents*)

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
    end_offset=700347,
    et=90065,
    filter='Hatchback Kia',
    group_id='towards',
    id='<ID>',
    limit=458049,
    lt=735287,
    offset=450824,
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

