# LogandTextual
(*logand_textual*)

### Available Operations

* [get](#get) - get the log message and textual diff for given commit

## get

get the log message and textual diff for given commit

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logand_textual.get(commit='<value>', group='<value>')

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

**[operations.GetLogandTextualResponse](../../models/operations/getlogandtextualresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
