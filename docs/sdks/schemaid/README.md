# SchemaID
(*schema_id*)

### Available Operations

* [delete](#delete) - Delete Schema
* [get](#get) - Get Schema by ID
* [update](#update) - Update Schema

## delete

Delete Schema

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.schema_id.delete(id='program')

if res.schema_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteSchemaIDResponse](../../models/operations/deleteschemaidresponse.md)**


## get

Get Schema by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.schema_id.get(id='female')

if res.schema_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetSchemaIDResponse](../../models/operations/getschemaidresponse.md)**


## update

Update Schema

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.schema_id.update(id='Van', schema_lib_entry=shared.SchemaLibEntry(
    additional_properties={
        "East": 'male',
    },
    id='<ID>',
    schema='Metal',
))

if res.schema_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique ID                                                                |
| `schema_lib_entry`                                                       | [Optional[shared.SchemaLibEntry]](../../models/shared/schemalibentry.md) | :heavy_minus_sign:                                                       | Schema object to be updated                                              |


### Response

**[operations.UpdateSchemaIDResponse](../../models/operations/updateschemaidresponse.md)**

