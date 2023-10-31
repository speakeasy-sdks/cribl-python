# TrustPolicies
(*trust_policies*)

### Available Operations

* [get](#get) - Get a list of TrustPolicy objects

## get

Get a list of TrustPolicy objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.trust_policies.get()

if res.trust_policies is not None:
    # handle response
    pass
```


### Response

**[operations.GetTrustPoliciesResponse](../../models/operations/gettrustpoliciesresponse.md)**

