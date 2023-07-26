# idp_auth

### Available Operations

* [get](#get) - Get IDP used for an authorization code callback

## get

Get IDP used for an authorization code callback

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetIDPAuthRequest(
    code='beatae',
    state='sunt',
)

res = s.idp_auth.get(req)

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetIDPAuthRequest](../../models/operations/getidpauthrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetIDPAuthResponse](../../models/operations/getidpauthresponse.md)**

