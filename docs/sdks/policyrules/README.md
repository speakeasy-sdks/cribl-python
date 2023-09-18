# PolicyRules

### Available Operations

* [get](#get) - Get a list of PolicyRule objects

## get

Get a list of PolicyRule objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.policy_rules.get()

if res.policy_rules is not None:
    # handle response
```


### Response

**[operations.GetPolicyRulesResponse](../../models/operations/getpolicyrulesresponse.md)**

