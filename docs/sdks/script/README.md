# script

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
    "neque": 'laudantium',
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

req = operations.DeleteScriptRequest(
    id='8e4d8039-ea5f-49b1-8a24-4fd619039dac',
)

res = s.script.delete(req)

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteScriptRequest](../../models/operations/deletescriptrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


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

req = operations.GetScriptRequest(
    id='d38ed0dc-671d-4c7f-9e3a-f15920c90d1b',
)

res = s.script.get(req)

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetScriptRequest](../../models/operations/getscriptrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


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

req = operations.UpdateScriptRequest(
    request_body={
        "natus": 'aperiam',
        "dicta": 'repellat',
    },
    id='2bd89c8a-3263-49da-9b7b-6902b881a94f',
)

res = s.script.update(req)

if res.script_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateScriptRequest](../../models/operations/updatescriptrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateScriptResponse](../../models/operations/updatescriptresponse.md)**

