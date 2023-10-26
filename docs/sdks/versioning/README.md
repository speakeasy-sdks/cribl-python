# Versioning
(*versioning*)

### Available Operations

* [get](#get) - Get info about versioning availability

## get

Get info about versioning availability

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.versioning.get()

if res.git_infos is not None:
    # handle response
    pass
```


### Response

**[operations.GetVersioningResponse](../../models/operations/getversioningresponse.md)**

