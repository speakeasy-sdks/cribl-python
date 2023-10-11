# AppscopeLibEntries
(*appscope_lib_entries*)

### Available Operations

* [get](#get) - Get a list of AppscopeLibEntry objects

## get

Get a list of AppscopeLibEntry objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.appscope_lib_entries.get()

if res.app_scope_lib_entries is not None:
    # handle response
```


### Response

**[operations.GetAppscopeLibEntriesResponse](../../models/operations/getappscopelibentriesresponse.md)**

