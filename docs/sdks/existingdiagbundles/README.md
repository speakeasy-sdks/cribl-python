# ExistingDiagBundles
(*existing_diag_bundles*)

### Available Operations

* [get](#get) - Get list of existing diag bundles

## get

Get list of existing diag bundles

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.existing_diag_bundles.get()

if res.existing_diag is not None:
    # handle response
```


### Response

**[operations.GetExistingDiagBundlesResponse](../../models/operations/getexistingdiagbundlesresponse.md)**

