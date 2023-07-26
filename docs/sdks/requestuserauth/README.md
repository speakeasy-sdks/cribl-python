# request_user_auth

### Available Operations

* [logout](#logout) - API call that the IDP should use for a logout request

## logout

API call that the IDP should use for a logout request

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.LogoutRequest(
    relay_state='quos',
    saml_response='illo',
)

res = s.request_user_auth.logout(req)

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.LogoutRequest](../../models/shared/logoutrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.LogoutRequestUserAuthResponse](../../models/operations/logoutrequestuserauthresponse.md)**

