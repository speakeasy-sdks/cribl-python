# WorkingTree
(*working_tree*)

### Available Operations

* [get](#get) - get the the working tree status

## get

get the the working tree status

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.working_tree.get(group='<value>')

if res.git_status_results is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group`            | *Optional[str]*    | :heavy_minus_sign: | Group ID           |


### Response

**[operations.GetWorkingTreeResponse](../../models/operations/getworkingtreeresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
