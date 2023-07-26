# list_cribl_version

### Available Operations

* [get](#get) - Get a list of Cribl versions available for upgrade

## get

Get a list of Cribl versions available for upgrade

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.list_cribl_version.get()

if res.upgrade_results is not None:
    # handle response
```


### Response

**[operations.GetListCriblVersionResponse](../../models/operations/getlistcriblversionresponse.md)**

