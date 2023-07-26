# list_global_variable

### Available Operations

* [get](#get) - Get a list of Global Variable objects

## get

Get a list of Global Variable objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.list_global_variable.get()

if res.global_vars is not None:
    # handle response
```


### Response

**[operations.GetListGlobalVariableResponse](../../models/operations/getlistglobalvariableresponse.md)**

