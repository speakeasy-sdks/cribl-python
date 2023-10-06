# RedirectInfo
(*redirect_info*)

### Available Operations

* [get](#get) - Obtain redirect information

## get

Obtain information needed to redirect users to the configured SSO IDP for authentication.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.redirect_info.get()

if res.redirect_info is not None:
    # handle response
```


### Response

**[operations.GetRedirectInfoResponse](../../models/operations/getredirectinforesponse.md)**

