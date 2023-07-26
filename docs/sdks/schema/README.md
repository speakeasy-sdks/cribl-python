# schema

### Available Operations

* [create](#create) - Create Schema
* [delete](#delete) - Delete Schema
* [get](#get) - Get Schema by ID
* [post](#post) - Create Schema
* [update](#update) - Update Schema

## create

Create Schema

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
    "dignissimos": 'corporis',
    "quo": 'nisi',
    "quo": 'inventore',
}

res = s.schema.create(req)

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateSchemaResponse](../../models/operations/createschemaresponse.md)**


## delete

Delete Schema

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteSchemaRequest(
    id='fe606d07-d2a9-4c87-ae50-c16661a1d913',
)

res = s.schema.delete(req)

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSchemaRequest](../../models/operations/deleteschemarequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSchemaResponse](../../models/operations/deleteschemaresponse.md)**


## get

Get Schema by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSchemaRequest(
    id='6a7e8d53-213f-43f6-9875-2db764c59f0a',
)

res = s.schema.get(req)

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSchemaRequest](../../models/operations/getschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSchemaResponse](../../models/operations/getschemaresponse.md)**


## post

Create Schema

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
    "ea": 'placeat',
    "necessitatibus": 'harum',
}

res = s.schema.post(req)

if res.schema_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostSchemaResponse](../../models/operations/postschemaresponse.md)**


## update

Update Schema

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateSchemaRequest(
    request_body={
        "culpa": 'pariatur',
        "laborum": 'consequuntur',
        "omnis": 'maxime',
        "officia": 'iusto',
    },
    id='9181c956-7166-43c5-b0b5-665163a36385',
)

res = s.schema.update(req)

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateSchemaRequest](../../models/operations/updateschemarequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateSchemaResponse](../../models/operations/updateschemaresponse.md)**

