# textual_diff

### Available Operations

* [get](#get) - get the textual diff for given commit

## get

get the textual diff for given commit

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetTextualDiffRequest(
    commit='eum',
    group='sint',
)

res = s.textual_diff.get(req)

if res.textual_diff is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTextualDiffRequest](../../models/operations/gettextualdiffrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTextualDiffResponse](../../models/operations/gettextualdiffresponse.md)**

