# cancel_running_group

### Available Operations

* [post](#post) - Cancel a running group upgrade

## post

Cancel a running group upgrade

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostCancelRunningGroupRequest(
    group='rem',
)

res = s.cancel_running_group.post(req)

if res.cancel_running_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PostCancelRunningGroupRequest](../../models/operations/postcancelrunninggrouprequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PostCancelRunningGroupResponse](../../models/operations/postcancelrunninggroupresponse.md)**

