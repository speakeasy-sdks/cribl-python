# Script
(*script*)

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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.ScriptLibEntry(
    additional_properties={
        'key': 'string',
    },
    args=[
        'string',
    ],
    command='string',
    env={
        'key': 'string',
    },
    id='<ID>',
)

res = s.script.create(req)

if res.script_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.ScriptLibEntry](../../models/components/scriptlibentry.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateScriptResponse](../../models/operations/createscriptresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## delete

Delete Script

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.script.delete(id='string')

if res.script_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteScriptResponse](../../models/operations/deletescriptresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get Script by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.script.get(id='string')

if res.script_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetScriptResponse](../../models/operations/getscriptresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update Script

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.script.update(id='string', script_lib_entry=components.ScriptLibEntry(
    additional_properties={
        'key': 'string',
    },
    args=[
        'string',
    ],
    command='string',
    env={
        'key': 'string',
    },
    id='<ID>',
))

if res.script_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | Unique ID                                                                        |
| `script_lib_entry`                                                               | [Optional[components.ScriptLibEntry]](../../models/components/scriptlibentry.md) | :heavy_minus_sign:                                                               | Script object to be updated                                                      |


### Response

**[operations.UpdateScriptResponse](../../models/operations/updatescriptresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
