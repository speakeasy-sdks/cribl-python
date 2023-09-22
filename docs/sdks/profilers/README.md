# Profilers

### Available Operations

* [get](#get) - Get a list of ProfilerItem objects

## get

Get a list of ProfilerItem objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.profilers.get()

if res.profiler_items is not None:
    # handle response
```


### Response

**[operations.GetProfilersResponse](../../models/operations/getprofilersresponse.md)**

