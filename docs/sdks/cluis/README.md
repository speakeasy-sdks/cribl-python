# Cluis
(*cluis*)

### Available Operations

* [get](#get) - Get CLUI search results

## get

Get CLUI search results

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.cluis.get(query='string', context='string')

if res.clui_items is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `query`                                         | *str*                                           | :heavy_check_mark:                              | Search query                                    |
| `context`                                       | *Optional[str]*                                 | :heavy_minus_sign:                              | Search query context, either "stream" or "edge" |


### Response

**[operations.GetCluisResponse](../../models/operations/getcluisresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
