# conditions

### Available Operations

* [get](#get) - Get a list of Condition objects

## get

Get a list of Condition objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.conditions.get()

if res.conditions is not None:
    # handle response
```


### Response

**[operations.GetConditionsResponse](../../models/operations/getconditionsresponse.md)**

