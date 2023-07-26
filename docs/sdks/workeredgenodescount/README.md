# worker_edge_nodes_count

### Available Operations

* [get](#get) - get worker and edge nodes count

## get

get worker and edge nodes count

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkerEdgeNodesCountRequest(
    filter_exp='a',
)

res = s.worker_edge_nodes_count.get(req)

if res.worker_edge_nodes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetWorkerEdgeNodesCountRequest](../../models/operations/getworkeredgenodescountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetWorkerEdgeNodesCountResponse](../../models/operations/getworkeredgenodescountresponse.md)**

