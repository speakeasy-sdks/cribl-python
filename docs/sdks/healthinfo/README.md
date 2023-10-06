# HealthInfo
(*health_info*)

### Available Operations

* [get](#get) - Provides health info for REST server

## get

Provides health info for REST server

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.health_info.get()

if res.health_status is not None:
    # handle response
```


### Response

**[operations.GetHealthInfoResponse](../../models/operations/gethealthinforesponse.md)**

