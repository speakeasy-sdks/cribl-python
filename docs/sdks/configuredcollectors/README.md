# configured_collectors

### Available Operations

* [get](#get) - Get list of configured collectors

## get

Get list of configured collectors

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.configured_collectors.get()

if res.configured_collectors is not None:
    # handle response
```


### Response

**[operations.GetConfiguredCollectorsResponse](../../models/operations/getconfiguredcollectorsresponse.md)**

