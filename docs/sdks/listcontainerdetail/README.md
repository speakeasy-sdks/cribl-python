# list_container_detail

### Available Operations

* [get](#get) - Get a detailed list of containers running on the edge host.

## get

Get a detailed list of containers running on the edge host.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.list_container_detail.get()

if res.containers is not None:
    # handle response
```


### Response

**[operations.GetListContainerDetailResponse](../../models/operations/getlistcontainerdetailresponse.md)**

