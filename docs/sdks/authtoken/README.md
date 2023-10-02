# AuthToken
(*auth_token*)

### Available Operations

* [login](#login) - Log in and obtain Auth token

## login

This endpoint is unavailable on Cribl.Cloud. Instead, get the Bearer token as detailed here: https://docs.cribl.io/stream/api-tutorials/#criblcloud-free-tier

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.LoginInfo(
    password='2bVVxb7UVU0peMp',
    username='Clyde.Parisian',
)

res = s.auth_token.login(req)

if res.auth_token is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.LoginInfo](../../models/shared/logininfo.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.LoginAuthTokenResponse](../../models/operations/loginauthtokenresponse.md)**

