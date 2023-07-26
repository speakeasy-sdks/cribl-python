# previous_cribl_package

### Available Operations

* [get](#get) - Get the previously downloaded Cribl package

## get

Get the previously downloaded Cribl package

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetPreviousCriblPackageRequest(
    file='culpa',
)

res = s.previous_cribl_package.get(req)

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetPreviousCriblPackageRequest](../../models/operations/getpreviouscriblpackagerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetPreviousCriblPackageResponse](../../models/operations/getpreviouscriblpackageresponse.md)**

