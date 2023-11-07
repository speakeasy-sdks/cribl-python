# Authorizations
(*.authorizations*)

### Available Operations

* [get](#get) - get the client's authorization policy

## get

get the client's authorization policy

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.authorizations.get()

if res.auth_policy_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetAuthorizationsResponse](../../models/operations/getauthorizationsresponse.md)**

