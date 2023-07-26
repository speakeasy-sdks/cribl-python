# log_file_contents

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
    end_offset=143976,
    et=291596,
    filter='maxime',
    group_id='maxime',
    id='b06c8ca1-2d02-4529-a70b-8d5722dd895b',
    limit=532721,
    lt=704665,
    offset=809212,
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

