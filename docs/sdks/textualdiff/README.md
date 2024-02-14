# TextualDiff
(*textual_diff*)

### Available Operations

* [get](#get) - get the textual diff for given commit

## get

get the textual diff for given commit

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.textual_diff.get(commit='string', group='string')

if res.textual_diff is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `commit`                      | *Optional[str]*               | :heavy_minus_sign:            | Commit hash (default is HEAD) |
| `group`                       | *Optional[str]*               | :heavy_minus_sign:            | Group ID                      |


### Response

**[operations.GetTextualDiffResponse](../../models/operations/gettextualdiffresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
