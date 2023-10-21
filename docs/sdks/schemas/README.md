# Schemas
(*schemas*)

### Available Operations

* [get](#get) - Get a list of Schema objects

## get

Get a list of Schema objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.schemas.get()

if res.schema_lib_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetSchemasResponse](../../models/operations/getschemasresponse.md)**

