# RedirectUserAuth
(*redirect_user_auth*)

### Available Operations

* [logout](#logout) - Redirect user to IDP with logout request

## logout

Redirect user to IDP with logout request

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.redirect_user_auth.logout()

if res.success is not None:
    # handle response
    pass
```


### Response

**[operations.LogoutRedirectUserAuthResponse](../../models/operations/logoutredirectuserauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Success   | 400,401          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
