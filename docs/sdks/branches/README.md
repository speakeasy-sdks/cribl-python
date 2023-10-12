# Branches
(*branches*)

### Available Operations

* [get](#get) - get the list of branches

## get

get the list of branches

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.branches.get()

if res.branches is not None:
    # handle response
```


### Response

**[operations.GetBranchesResponse](../../models/operations/getbranchesresponse.md)**

