# RedirectInfo
(*redirect_info*)

### Available Operations

* [get](#get) - Obtain redirect information

## get

Obtain information needed to redirect users to the configured SSO IDP for authentication.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.redirect_info.get()

if res.redirect_info is not None:
    # handle response
    pass

```


### Response

**[operations.GetRedirectInfoResponse](../../models/operations/getredirectinforesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
