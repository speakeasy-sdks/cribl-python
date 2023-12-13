# ClientRoles
(*client_roles*)

### Available Operations

* [get](#get) - get the client's roles

## get

get the client's roles

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.client_roles.get()

if res.client_role_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetClientRolesResponse](../../models/operations/getclientrolesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
