# GlobalVariable
(*.global_variable*)

### Available Operations

* [post](#post) - Create Global Variable

## post

Create Global Variable

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.GlobalVar(
    id='<ID>',
    value='string',
)

res = s.global_variable.post(req)

if res.global_vars is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [components.GlobalVar](../../models/shared/globalvar.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.PostGlobalVariableResponse](../../models/operations/postglobalvariableresponse.md)**

