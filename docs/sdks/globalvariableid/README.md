# global_variable_id

### Available Operations

* [delete](#delete) - Delete Global Variable
* [get](#get) - Get Global Variable by ID
* [update](#update) - Update Global Variable

## delete

Delete Global Variable

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteGlobalVariableIDRequest(
    id='7cbdb6ee-c743-478b-a253-17747dc915ad',
)

res = s.global_variable_id.delete(req)

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteGlobalVariableIDRequest](../../models/operations/deleteglobalvariableidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteGlobalVariableIDResponse](../../models/operations/deleteglobalvariableidresponse.md)**


## get

Get Global Variable by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetGlobalVariableIDRequest(
    id='2caf5dd6-723d-4c0f-9ae2-f3a6b7008787',
)

res = s.global_variable_id.get(req)

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetGlobalVariableIDRequest](../../models/operations/getglobalvariableidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetGlobalVariableIDResponse](../../models/operations/getglobalvariableidresponse.md)**


## update

Update Global Variable

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateGlobalVariableIDRequest(
    global_var=shared.GlobalVar(
        description='quis',
        id='6143f5a6-c98b-4555-9408-0d40bcacc6cb',
        lib='fugiat',
        tags='laboriosam',
        type=shared.GlobalVarType.EXPRESSION,
        value='enim',
    ),
    id='f3ec9093-04f9-426b-ad25-53819b474b0e',
)

res = s.global_variable_id.update(req)

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateGlobalVariableIDRequest](../../models/operations/updateglobalvariableidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.UpdateGlobalVariableIDResponse](../../models/operations/updateglobalvariableidresponse.md)**

