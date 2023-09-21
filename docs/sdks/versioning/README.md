# Versioning

### Available Operations

* [get](#get) - Get info about versioning availability

## get

Get info about versioning availability

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.versioning.get()

if res.git_infos is not None:
    # handle response
```


### Response

**[operations.GetVersioningResponse](../../models/operations/getversioningresponse.md)**

