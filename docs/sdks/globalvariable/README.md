# global_variable

### Available Operations

* [post](#post) - Create Global Variable

## post

Create Global Variable

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.GlobalVar(
    description='illum',
    id='8bb31180-f739-4ae9-a057-eb809e281033',
    lib='sunt',
    tags='a',
    type=shared.GlobalVarType.NUMBER,
    value='occaecati',
)

res = s.global_variable.post(req)

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.GlobalVar](../../models/shared/globalvar.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.PostGlobalVariableResponse](../../models/operations/postglobalvariableresponse.md)**

