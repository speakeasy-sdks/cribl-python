# SchemaID

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.schema_id.delete(id='minus')

if res.schema_lib_entries is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.schema_id.get(id='quo')

if res.schema_lib_entries is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.schema_id.update(id='quos', request_body={
    "asperiores": 'voluptatum',
})

if res.schema_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `id`                        | *str*                       | :heavy_check_mark:          | Unique ID                   |
| `request_body`              | dict[str, *Any*]            | :heavy_minus_sign:          | Schema object to be updated |


### Response

**[operations.UpdateSchemaIDResponse](../../models/operations/updateschemaidresponse.md)**

