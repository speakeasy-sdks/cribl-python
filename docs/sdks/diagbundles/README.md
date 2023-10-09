# DiagBundles
(*diag_bundles*)

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


res = s.diag_bundles.get()

if res.get_diag_bundles_200_application_tar_plus_gzip_binary_string is not None:
    # handle response
```


### Response

**[operations.GetDiagBundlesResponse](../../models/operations/getdiagbundlesresponse.md)**

