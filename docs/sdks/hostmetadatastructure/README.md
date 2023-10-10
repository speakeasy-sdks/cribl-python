# HostMetadataStructure
(*host_metadata_structure*)

### Available Operations

* [get](#get) - Get the host's metadata structure

## get

Get the host's metadata structure

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.host_metadata_structure.get()

if res.edge_metadatas is not None:
    # handle response
```


### Response

**[operations.GetHostMetadataStructureResponse](../../models/operations/gethostmetadatastructureresponse.md)**

