# UserAuth
(*user_auth*)

### Available Operations

* [logout](#logout) - Log current user out

## logout

Log current user out

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_auth.logout()

if res.success is not None:
    # handle response
    pass

```


### Response

**[operations.LogoutUserAuthResponse](../../models/operations/logoutuserauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
