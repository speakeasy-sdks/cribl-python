# DistributedDeployment

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


res = s.distributed_deployment.get(mode='veritatis')

if res.distributed_summaries is not None:
    # handle response
```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `mode`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Filter for worker/group type, either "worker" for Stream or "managed-edge" for Edge |


### Response

**[operations.GetDistributedDeploymentResponse](../../models/operations/getdistributeddeploymentresponse.md)**

