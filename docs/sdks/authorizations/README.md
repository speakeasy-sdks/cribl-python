# Authorizations
(*authorizations*)

### Available Operations

* [get](#get) - get the client's authorization policy

## get

get the client's authorization policy

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.authorizations.get()

if res.auth_policy_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetAuthorizationsResponse](../../models/operations/getauthorizationsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
