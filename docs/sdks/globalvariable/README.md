# GlobalVariable
(*global_variable*)

### Available Operations

* [post](#post) - Create Global Variable

## post

Create Global Variable

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.GlobalVar(
    id='<id>',
    value='<value>',
)

res = s.global_variable.post(req)

if res.global_vars is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.GlobalVar](../../models/components/globalvar.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostGlobalVariableResponse](../../models/operations/postglobalvariableresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
