# Features
(*features*)

### Available Operations

* [get](#get) - List all features

## get

List all features

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.features.get()

if res.features_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetFeaturesResponse](../../models/operations/getfeaturesresponse.md)**

