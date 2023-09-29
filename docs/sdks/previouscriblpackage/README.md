# PreviousCriblPackage
(*previous_cribl_package*)

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


res = s.previous_cribl_package.get(file='female')

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `file`                            | *str*                             | :heavy_check_mark:                | Name of the file to be downloaded |


### Response

**[operations.GetPreviousCriblPackageResponse](../../models/operations/getpreviouscriblpackageresponse.md)**

