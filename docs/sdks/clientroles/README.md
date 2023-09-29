# ClientRoles
(*client_roles*)

### Available Operations

* [get](#get) - get the client's roles

## get

get the client's roles

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.client_roles.get()

if res.client_role_entries is not None:
    # handle response
```


### Response

**[operations.GetClientRolesResponse](../../models/operations/getclientrolesresponse.md)**

