# Script

### Available Operations

* [create](#create) - Create Script
* [delete](#delete) - Delete Script
* [get](#get) - Get Script by ID
* [update](#update) - Update Script

## create

Create Script

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = {
    "neque": 'odit',
}

res = s.script.create(req)

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateScriptResponse](../../models/operations/createscriptresponse.md)**


## delete

Delete Script

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.script.delete(id='earum')

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteScriptResponse](../../models/operations/deletescriptresponse.md)**


## get

Get Script by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.script.get(id='veniam')

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetScriptResponse](../../models/operations/getscriptresponse.md)**


## update

Update Script

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.script.update(id='ipsam', request_body={
    "eaque": 'exercitationem',
})

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `id`                        | *str*                       | :heavy_check_mark:          | Unique ID                   |
| `request_body`              | dict[str, *Any*]            | :heavy_minus_sign:          | Script object to be updated |


### Response

**[operations.UpdateScriptResponse](../../models/operations/updatescriptresponse.md)**

