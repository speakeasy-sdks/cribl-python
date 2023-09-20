# GlobalVariable

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
    description='nesciunt',
    id='a8d8f5c0-b2f2-4fb7-b194-a276b26916fe',
    lib='illo',
    tags='reiciendis',
    type=shared.GlobalVarType.STRING,
    value='corrupti',
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

