# LatestPQ
(*latest_pq*)

### Available Operations

* [get](#get) - Get status of latest clear PQ job for an output

## get

Get status of latest clear PQ job for an output

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.latest_pq.get(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.GetLatestPQResponse](../../models/operations/getlatestpqresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
