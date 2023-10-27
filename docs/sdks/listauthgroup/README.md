# ListAuthGroup
(*list_auth_group*)

### Available Operations

* [get](#get) - List the external authentication system's groups

## get

List the external authentication system's groups

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.list_auth_group.get()

if res.crud_entity_bases is not None:
    # handle response
    pass
```


### Response

**[operations.GetListAuthGroupResponse](../../models/operations/getlistauthgroupresponse.md)**

