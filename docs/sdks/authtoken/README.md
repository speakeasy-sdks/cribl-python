# AuthToken
(*auth_token*)

### Available Operations

* [login](#login) - Log in and obtain Auth token

## login

This endpoint is unavailable on Cribl.Cloud. Instead, get the Bearer token as detailed here: https://docs.cribl.io/stream/api-tutorials/#criblcloud-free-tier

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl()

req = components.LoginInfo(
    password='2bVVxb7UVU0peMp',
    username='Clyde.Parisian',
)

res = s.auth_token.login(req)

if res.auth_token is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.LoginInfo](../../models/components/logininfo.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.LoginAuthTokenResponse](../../models/operations/loginauthtokenresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,403,429      | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
