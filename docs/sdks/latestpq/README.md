# latest_pq

### Available Operations

* [get](#get) - Get status of latest clear PQ job for an output

## get

Get status of latest clear PQ job for an output

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetLatestPQRequest(
    id='230f841f-b1bd-423f-9b14-db6be5a68599',
)

res = s.latest_pq.get(req)

if res.get_latest_pq_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetLatestPQRequest](../../models/operations/getlatestpqrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetLatestPQResponse](../../models/operations/getlatestpqresponse.md)**

