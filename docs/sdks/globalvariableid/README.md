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

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.global_variable_id.delete(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get

Get Global Variable by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.global_variable_id.get(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## update

Update Global Variable

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.global_variable_id.update(id='<value>', global_var=components.GlobalVar(
    id='<id>',
    value='<value>',
))

if res.global_vars is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique ID                                                              |
| `global_var`                                                           | [Optional[components.GlobalVar]](../../models/components/globalvar.md) | :heavy_minus_sign:                                                     | Global Variable object to be updated                                   |


### Response

**[operations.UpdateGlobalVariableIDResponse](../../models/operations/updateglobalvariableidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
