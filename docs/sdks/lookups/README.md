# Lookups
(*lookups*)

### Available Operations

* [get](#get) - Get a list of LookupFile objects

## get

Get a list of LookupFile objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.lookups.get()

if res.lookup_files is not None:
    # handle response
    pass
```


### Response

**[operations.GetLookupsResponse](../../models/operations/getlookupsresponse.md)**

