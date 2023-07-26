# process_running_detail

### Available Operations

* [get](#get) - Get details of a process running on the edge host

## get

Get details of a process running on the edge host

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetProcessRunningDetailRequest(
    pid='ipsa',
)

res = s.process_running_detail.get(req)

if res.processes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetProcessRunningDetailRequest](../../models/operations/getprocessrunningdetailrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetProcessRunningDetailResponse](../../models/operations/getprocessrunningdetailresponse.md)**

