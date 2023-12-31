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


res = s.worker_edge_nodes.get('unde', 365473, 213405, 'rerum')

if res.master_worker_entries is not None:
    # handle response
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

