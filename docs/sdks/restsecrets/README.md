# rest_secrets

### Available Operations

* [get](#get) - Get a list of RestSecret objects

## get

Get a list of RestSecret objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.rest_secrets.get()

if res.rest_secrets is not None:
    # handle response
```


### Response

**[operations.GetRestSecretsResponse](../../models/operations/getrestsecretsresponse.md)**

