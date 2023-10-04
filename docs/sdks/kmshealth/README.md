# KMSHealth
(*kms_health*)

### Available Operations

* [get](#get) - Get Cribl KMS health

## get

Get Cribl KMS health

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.kms_health.get()

if res.kms_health is not None:
    # handle response
```


### Response

**[operations.GetKMSHealthResponse](../../models/operations/getkmshealthresponse.md)**

