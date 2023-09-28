# LatestPQ
(*latest_pq*)

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


res = s.latest_pq.get(id='distinctio')

if res.get_latest_pq_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.GetLatestPQResponse](../../models/operations/getlatestpqresponse.md)**

