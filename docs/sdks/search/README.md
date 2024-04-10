# Search
(*search*)

### Available Operations

* [dispatch_search](#dispatch_search) - Dispatch search *id* to worker nodes filtered by worker node filter using RPC

## dispatch_search

Dispatch search *id* to worker nodes filtered by worker node filter using RPC

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search.dispatch_search(id='<value>')

if res.search_id is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.DispatchSearchResponse](../../models/operations/dispatchsearchresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
