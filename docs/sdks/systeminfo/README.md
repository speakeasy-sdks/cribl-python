# SystemInfo

### Available Operations

* [get](#get) - Get basic system information

## get

Get basic system information

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.system_info.get()

if res.system_info_objects is not None:
    # handle response
```


### Response

**[operations.GetSystemInfoResponse](../../models/operations/getsysteminforesponse.md)**

