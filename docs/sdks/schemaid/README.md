# schema_id

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

req = operations.DeleteSchemaIDRequest(
    id='12ab2521-b9f2-4e07-a467-b8a40bc05fab',
)

res = s.schema_id.delete(req)

if res.schema_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteSchemaIDRequest](../../models/operations/deleteschemaidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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

req = operations.GetSchemaIDRequest(
    id='0d650edf-22a9-44d2-8ec9-0ea41d1f465e',
)

res = s.schema_id.get(req)

if res.schema_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSchemaIDRequest](../../models/operations/getschemaidrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


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

req = operations.UpdateSchemaIDRequest(
    request_body={
        "veniam": 'ab',
        "minima": 'nisi',
        "repellat": 'sapiente',
    },
    id='f73fdf54-fdd5-4ea9-9433-98dafb42a8d6',
)

res = s.schema_id.update(req)

if res.schema_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateSchemaIDRequest](../../models/operations/updateschemaidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateSchemaIDResponse](../../models/operations/updateschemaidresponse.md)**

