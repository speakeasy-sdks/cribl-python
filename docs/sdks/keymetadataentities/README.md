# KeyMetadataEntities

### Available Operations

* [get](#get) - Get a list of KeyMetadataEntity objects

## get

Get a list of KeyMetadataEntity objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.key_metadata_entities.get()

if res.key_metadata_entities is not None:
    # handle response
```


### Response

**[operations.GetKeyMetadataEntitiesResponse](../../models/operations/getkeymetadataentitiesresponse.md)**

