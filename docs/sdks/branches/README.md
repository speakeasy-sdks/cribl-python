# Branches
(*branches*)

### Available Operations

* [get](#get) - get the list of branches

## get

get the list of branches

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.branches.get()

if res.branches is not None:
    # handle response
    pass

```


### Response

**[operations.GetBranchesResponse](../../models/operations/getbranchesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
