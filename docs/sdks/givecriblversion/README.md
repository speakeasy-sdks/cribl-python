# give_cribl_version

### Available Operations

* [post](#post) - Upgrade Cribl to a given version

## post

Upgrade Cribl to a given version

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostGiveCriblVersionRequest(
    version='labore',
)

res = s.give_cribl_version.post(req)

if res.cribl is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PostGiveCriblVersionRequest](../../models/operations/postgivecriblversionrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PostGiveCriblVersionResponse](../../models/operations/postgivecriblversionresponse.md)**

