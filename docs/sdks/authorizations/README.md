# Authorizations

### Available Operations

* [get](#get) - get the client's authorization policy

## get

get the client's authorization policy

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.authorizations.get()

if res.auth_policy_entries is not None:
    # handle response
```


### Response

**[operations.GetAuthorizationsResponse](../../models/operations/getauthorizationsresponse.md)**

