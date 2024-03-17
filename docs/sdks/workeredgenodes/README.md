# WorkerEdgeNodes
(*worker_edge_nodes*)

### Available Operations

* [get](#get) - get worker and edge nodes
* [restarts](#restarts) - restarts worker nodes

## get

get worker and edge nodes

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.worker_edge_nodes.get(filter_exp='<value>', limit=700347, offset=90065, sort_exp='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## restarts

restarts worker nodes

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.worker_edge_nodes.restarts()

if res.restart_responses is not None:
    # handle response
    pass

```


### Response

**[operations.RestartsWorkerEdgeNodesResponse](../../models/operations/restartsworkeredgenodesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
