# LogandTextual

### Available Operations

* [get](#get) - get the log message and textual diff for given commit

## get

get the log message and textual diff for given commit

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.logand_textual.get(commit='debitis', group='voluptatem')

if res.textual_diff is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `commit`                      | *Optional[str]*               | :heavy_minus_sign:            | Commit hash (default is HEAD) |
| `group`                       | *Optional[str]*               | :heavy_minus_sign:            | Group ID                      |


### Response

**[operations.GetLogandTextualResponse](../../models/operations/getlogandtextualresponse.md)**

