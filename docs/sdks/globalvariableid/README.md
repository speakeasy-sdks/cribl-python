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


res = s.global_variable_id.delete('atque')

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.global_variable_id.get('beatae')

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.global_variable_id.update('at', shared.GlobalVar(
    description='labore',
    id='c700b607-f3c9-43c7-bb9d-a3f2ceda7e23',
    lib='repellat',
    tags='explicabo',
    type=shared.GlobalVarType.STRING,
    value='exercitationem',
))

if res.global_vars is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | Unique ID                                                      |
| `global_var`                                                   | [Optional[shared.GlobalVar]](../../models/shared/globalvar.md) | :heavy_minus_sign:                                             | Global Variable object to be updated                           |


### Response

**[operations.UpdateGlobalVariableIDResponse](../../models/operations/updateglobalvariableidresponse.md)**

