# ListSchema

### Available Operations

* [get](#get) - Get a list of Schema objects

## get

Get a list of Schema objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.list_schema.get()

if res.schema_lib_entries is not None:
    # handle response
```


### Response

**[operations.GetListSchemaResponse](../../models/operations/getlistschemaresponse.md)**

