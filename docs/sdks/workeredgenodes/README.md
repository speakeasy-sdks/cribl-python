# WorkerEdgeNodes
(*.worker_edge_nodes*)

### Available Operations

* [get](#get) - get worker and edge nodes
* [restarts](#restarts) - restarts worker nodes

## get

get worker and edge nodes

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.worker_edge_nodes.get(filter_exp='string', limit=700347, offset=90065, sort_exp='string')

if res.master_worker_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `filter_exp`                               | *Optional[str]*                            | :heavy_minus_sign:                         | Filter expression evaluated against nodes  |
| `limit`                                    | *Optional[int]*                            | :heavy_minus_sign:                         | Maximum number of nodes to return          |
| `offset`                                   | *Optional[int]*                            | :heavy_minus_sign:                         | Pagination offset                          |
| `sort_exp`                                 | *Optional[str]*                            | :heavy_minus_sign:                         | Sorting expression evaluated against nodes |


### Response

**[operations.GetWorkerEdgeNodesResponse](../../models/operations/getworkeredgenodesresponse.md)**


## restarts

restarts worker nodes

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.worker_edge_nodes.restarts()

if res.restart_responses is not None:
    # handle response
    pass
```


### Response

**[operations.RestartsWorkerEdgeNodesResponse](../../models/operations/restartsworkeredgenodesresponse.md)**

