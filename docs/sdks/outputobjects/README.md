# OutputObjects
(*output_objects*)

### Available Operations

* [get](#get) - Get a list of Output objects

## get

Get a list of Output objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.output_objects.get()

if res.outputs is not None:
    # handle response
```


### Response

**[operations.GetOutputObjectsResponse](../../models/operations/getoutputobjectsresponse.md)**

