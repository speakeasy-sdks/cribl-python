# working_tree

### Available Operations

* [get](#get) - get the the working tree status

## get

get the the working tree status

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkingTreeRequest(
    group='ad',
)

res = s.working_tree.get(req)

if res.git_status_results is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetWorkingTreeRequest](../../models/operations/getworkingtreerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetWorkingTreeResponse](../../models/operations/getworkingtreeresponse.md)**

