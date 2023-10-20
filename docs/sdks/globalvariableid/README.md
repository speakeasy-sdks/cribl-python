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
    bearer_auth="",
)


res = s.global_variable_id.delete(id='program')

if res.global_vars is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.global_variable_id.get(id='female')

if res.global_vars is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.global_variable_id.update(id='Van', global_var=shared.GlobalVar(
    id='<ID>',
    value='East',
))

if res.global_vars is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | Unique ID                                                      |
| `global_var`                                                   | [Optional[shared.GlobalVar]](../../models/shared/globalvar.md) | :heavy_minus_sign:                                             | Global Variable object to be updated                           |


### Response

**[operations.UpdateGlobalVariableIDResponse](../../models/operations/updateglobalvariableidresponse.md)**

