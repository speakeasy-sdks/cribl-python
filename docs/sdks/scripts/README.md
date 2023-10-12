# Scripts
(*scripts*)

### Available Operations

* [get](#get) - Get a list of Script objects

## get

Get a list of Script objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.scripts.get()

if res.script_lib_entries is not None:
    # handle response
```


### Response

**[operations.GetScriptsResponse](../../models/operations/getscriptsresponse.md)**

