# idp_user_auth

### Available Operations

* [logout](#logout) - Accepts a logout request from an IDP and logs out the user

## logout

Accepts a logout request from an IDP and logs out the user

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.LogoutIDPUserAuthRequest(
    relay_state='molestias',
    saml_response='beatae',
)

res = s.idp_user_auth.logout(req)

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.LogoutIDPUserAuthRequest](../../models/operations/logoutidpuserauthrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.LogoutIDPUserAuthResponse](../../models/operations/logoutidpuserauthresponse.md)**

