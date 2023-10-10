# EdgeHostFiles
(*edge_host_files*)

### Available Operations

* [get](#get) - Get details about a file on the edge host.

## get

Get details about a file on the edge host.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.edge_host_files.get()

if res.edge_host_files is not None:
    # handle response
```


### Response

**[operations.GetEdgeHostFilesResponse](../../models/operations/getedgehostfilesresponse.md)**

