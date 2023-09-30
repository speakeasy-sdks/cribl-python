# Packs
(*packs*)

### Available Operations

* [get](#get) - Get info on packs

## get

Get info on packs

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.packs.get()

if res.pack_infos is not None:
    # handle response
```


### Response

**[operations.GetPacksResponse](../../models/operations/getpacksresponse.md)**

