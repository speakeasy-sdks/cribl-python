# licenses

### Available Operations

* [get](#get) - Get a list of License objects

## get

Get a list of License objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.licenses.get()

if res.licenses is not None:
    # handle response
```


### Response

**[operations.GetLicensesResponse](../../models/operations/getlicensesresponse.md)**

