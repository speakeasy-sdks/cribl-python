# Certificates
(*certificates*)

### Available Operations

* [get](#get) - Get a list of Certificate objects

## get

Get a list of Certificate objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.certificates.get()

if res.certificates is not None:
    # handle response
```


### Response

**[operations.GetCertificatesResponse](../../models/operations/getcertificatesresponse.md)**

