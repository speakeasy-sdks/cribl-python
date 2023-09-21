# SearchLimits

### Available Operations

* [get](#get) - Get search limits

## get

Get search limits

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.search_limits.get()

if res.search_settingses is not None:
    # handle response
```


### Response

**[operations.GetSearchLimitsResponse](../../models/operations/getsearchlimitsresponse.md)**

