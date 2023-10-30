# TextualDiff
(*textual_diff*)

### Available Operations

* [get](#get) - get the textual diff for given commit

## get

get the textual diff for given commit

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
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

