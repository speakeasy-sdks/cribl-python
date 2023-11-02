# UserAuth
(*user_auth*)

### Available Operations

* [logout](#logout) - Log current user out

## logout

Log current user out

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.user_auth.logout()

if res.success is not None:
    # handle response
    pass
```


### Response

**[operations.LogoutUserAuthResponse](../../models/operations/logoutuserauthresponse.md)**

