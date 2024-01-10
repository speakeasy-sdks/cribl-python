# PolicyRules
(*policy_rules*)

### Available Operations

* [get](#get) - Get a list of PolicyRule objects

## get

Get a list of PolicyRule objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.policy_rules.get()

if res.policy_rules is not None:
    # handle response
    pass
```


### Response

**[operations.GetPolicyRulesResponse](../../models/operations/getpolicyrulesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
