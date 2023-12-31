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


res = s.worker_edge_nodes_count.get('ut')

if res.worker_edge_nodes is not None:
    # handle response
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `filter_exp`                              | *Optional[str]*                           | :heavy_minus_sign:                        | Filter expression evaluated against nodes |


### Response

**[operations.GetWorkerEdgeNodesCountResponse](../../models/operations/getworkeredgenodescountresponse.md)**

