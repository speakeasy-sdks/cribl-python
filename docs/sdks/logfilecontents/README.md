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
    end_offset=848151,
    et=52508,
    filter='earum',
    group_id='perspiciatis',
    id='fe6c632c-a3ae-4d01-9799-6312fde04771',
    limit=479754,
    lt=457059,
    offset=508390,
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

