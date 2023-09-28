# GlobalVariableID
(*global_variable_id*)

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


res = s.global_variable_id.delete(id='maiores')

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


res = s.global_variable_id.get(id='incidunt')

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


res = s.global_variable_id.update(id='sed', global_var=shared.GlobalVar(
    description='provident',
    id='4e3698f4-47f6-403e-8b44-5e80ca55efd2',
    lib='aperiam',
    tags='saepe',
    type=shared.GlobalVarType.NUMBER,
    value='veniam',
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

