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


res = s.idp_user_auth.logout(relay_state='fuga', saml_response='praesentium')

if res.success is not None:
    # handle response
```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `relay_state`         | *Optional[str]*       | :heavy_minus_sign:    | N/A                   |
| `saml_response`       | *Optional[str]*       | :heavy_minus_sign:    | Logout request object |


### Response

**[operations.LogoutIDPUserAuthResponse](../../models/operations/logoutidpuserauthresponse.md)**

