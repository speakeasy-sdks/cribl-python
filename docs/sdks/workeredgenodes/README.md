# worker_edge_nodes

### Available Operations

* [get](#get) - get worker and edge nodes
* [restarts](#restarts) - restarts worker nodes

## get

get worker and edge nodes

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkerEdgeNodesRequest(
    filter_exp='quos',
    limit=568323,
    offset=431712,
    sort_exp='rerum',
)

res = s.worker_edge_nodes.get(req)

if res.master_worker_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetWorkerEdgeNodesRequest](../../models/operations/getworkeredgenodesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetWorkerEdgeNodesResponse](../../models/operations/getworkeredgenodesresponse.md)**


## restarts

restarts worker nodes

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.worker_edge_nodes.restarts()

if res.restart_responses is not None:
    # handle response
```


### Response

**[operations.RestartsWorkerEdgeNodesResponse](../../models/operations/restartsworkeredgenodesresponse.md)**

