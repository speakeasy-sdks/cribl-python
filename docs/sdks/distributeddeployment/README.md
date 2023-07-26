# distributed_deployment

### Available Operations

* [get](#get) - Get summary of Distributed deployment

## get

Get summary of Distributed deployment

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDistributedDeploymentRequest(
    mode='impedit',
)

res = s.distributed_deployment.get(req)

if res.distributed_summaries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetDistributedDeploymentRequest](../../models/operations/getdistributeddeploymentrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetDistributedDeploymentResponse](../../models/operations/getdistributeddeploymentresponse.md)**

