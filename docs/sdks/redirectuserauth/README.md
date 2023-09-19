# RedirectUserAuth

### Available Operations

* [logout](#logout) - Redirect user to IDP with logout request

## logout

Redirect user to IDP with logout request

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.redirect_user_auth.logout()

if res.success is not None:
    # handle response
```


### Response

**[operations.LogoutRedirectUserAuthResponse](../../models/operations/logoutredirectuserauthresponse.md)**

