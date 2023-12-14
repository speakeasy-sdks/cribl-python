# RequestUserAuth
(*request_user_auth*)

### Available Operations

* [logout](#logout) - API call that the IDP should use for a logout request

## logout

API call that the IDP should use for a logout request

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.LogoutRequest()

res = s.request_user_auth.logout(req)

if res.success is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.LogoutRequest](../../models/components/logoutrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.LogoutRequestUserAuthResponse](../../models/operations/logoutrequestuserauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400,401,429      | application/json |
| errors.SDKError  | 400-600          | */*              |
