# logand_textual

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

req = operations.GetLogandTextualRequest(
    commit='dolor',
    group='nostrum',
)

res = s.logand_textual.get(req)

if res.textual_diff is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetLogandTextualRequest](../../models/operations/getlogandtextualrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetLogandTextualResponse](../../models/operations/getlogandtextualresponse.md)**

