# TrustPolicies
(*trust_policies*)

### Available Operations

* [get](#get) - Get a list of TrustPolicy objects

## get

Get a list of TrustPolicy objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.trust_policies.get()

if res.trust_policies is not None:
    # handle response
    pass
```


### Response

**[operations.GetTrustPoliciesResponse](../../models/operations/gettrustpoliciesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
