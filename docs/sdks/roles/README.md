# Roles
(*roles*)

### Available Operations

* [get](#get) - Get a list of Role objects

## get

Get a list of Role objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.roles.get()

if res.roles is not None:
    # handle response
    pass
```


### Response

**[operations.GetRolesResponse](../../models/operations/getrolesresponse.md)**

