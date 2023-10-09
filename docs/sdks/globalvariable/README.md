# GlobalVariable
(*global_variable*)

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
    id='<ID>',
    value='Producer base',
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

