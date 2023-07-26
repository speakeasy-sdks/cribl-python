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
    end_offset=369523,
    et=60,
    filter='suscipit',
    group_id='deserunt',
    id='8aa94c02-644c-4f5e-9d9a-4578adc1ac60',
    limit=31574,
    lt=816421,
    offset=901008,
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

