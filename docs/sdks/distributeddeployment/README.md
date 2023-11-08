# DistributedDeployment
(*.distributed_deployment*)

### Available Operations

* [get](#get) - Get summary of Distributed deployment

## get

Get summary of Distributed deployment

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.distributed_deployment.get(mode='string')

if res.distributed_summaries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `mode`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Filter for worker/group type, either "worker" for Stream or "managed-edge" for Edge |


### Response

**[operations.GetDistributedDeploymentResponse](../../models/operations/getdistributeddeploymentresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
