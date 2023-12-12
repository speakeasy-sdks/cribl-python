# IDPUserAuth
(*idp_user_auth*)

### Available Operations

* [logout](#logout) - Accepts a logout request from an IDP and logs out the user

## logout

Accepts a logout request from an IDP and logs out the user

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.idp_user_auth.logout(relay_state='string', saml_response='string')

if res.success is not None:
    # handle response
    pass
```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `relay_state`         | *Optional[str]*       | :heavy_minus_sign:    | N/A                   |
| `saml_response`       | *Optional[str]*       | :heavy_minus_sign:    | Logout request object |


### Response

**[operations.LogoutIDPUserAuthResponse](../../models/operations/logoutidpuserauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400,401,429      | application/json |
| errors.SDKError  | 400-600          | */*              |
