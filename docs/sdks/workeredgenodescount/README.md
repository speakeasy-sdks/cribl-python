# WorkerEdgeNodesCount
(*worker_edge_nodes_count*)

### Available Operations

* [get](#get) - get worker and edge nodes count

## get

get worker and edge nodes count

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.worker_edge_nodes_count.get(filter_exp='<value>')

if res.worker_edge_nodes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `filter_exp`                              | *Optional[str]*                           | :heavy_minus_sign:                        | Filter expression evaluated against nodes |


### Response

**[operations.GetWorkerEdgeNodesCountResponse](../../models/operations/getworkeredgenodescountresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
