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
    "quo": 'suscipit',
    "ex": 'sint',
    "est": 'doloribus',
    "provident": 'alias',
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


res = s.schema.delete(id='deserunt')

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.schema.get(id='fugit')

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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
    "quo": 'molestiae',
    "maxime": 'facere',
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


res = s.schema.update(id='impedit', request_body={
    "deleniti": 'quasi',
    "maiores": 'voluptatem',
    "aliquid": 'laudantium',
})

if res.schema_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `id`                        | *str*                       | :heavy_check_mark:          | Unique ID                   |
| `request_body`              | dict[str, *Any*]            | :heavy_minus_sign:          | Schema object to be updated |


### Response

**[operations.UpdateSchemaResponse](../../models/operations/updateschemaresponse.md)**

