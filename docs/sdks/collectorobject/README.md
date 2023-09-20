# CollectorObject

### Available Operations

* [get](#get) - Get a list of Collector objects

## get

Get a list of Collector objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.collector_object.get()

if res.collectors is not None:
    # handle response
```


### Response

**[operations.GetCollectorObjectResponse](../../models/operations/getcollectorobjectresponse.md)**

