# DistributedDeployment
(*distributed_deployment*)

### Available Operations

* [get](#get) - Get summary of Distributed deployment

## get

Get summary of Distributed deployment

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.distributed_deployment.get(mode='<value>')

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
| errors.SDKError  | 4xx-5xx          | */*              |
