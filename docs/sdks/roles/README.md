# roles

### Available Operations

* [get](#get) - Get a list of Role objects

## get

Get a list of Role objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.roles.get()

if res.roles is not None:
    # handle response
```


### Response

**[operations.GetRolesResponse](../../models/operations/getrolesresponse.md)**

