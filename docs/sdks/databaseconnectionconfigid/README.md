# database_connection_config_id

### Available Operations

* [delete](#delete) - Delete DatabaseConnectionConfig
* [get](#get) - Get DatabaseConnectionConfig by ID
* [update](#update) - Update DatabaseConnectionConfig

## delete

Delete DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteDatabaseConnectionConfigIDRequest(
    id='f2257411-faf4-4b75-84e4-72e802857a5b',
)

res = s.database_connection_config_id.delete(req)

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteDatabaseConnectionConfigIDRequest](../../models/operations/deletedatabaseconnectionconfigidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteDatabaseConnectionConfigIDResponse](../../models/operations/deletedatabaseconnectionconfigidresponse.md)**


## get

Get DatabaseConnectionConfig by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDatabaseConnectionConfigIDRequest(
    id='40463a7d-575f-4140-8e76-4ad7334ec1b7',
)

res = s.database_connection_config_id.get(req)

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetDatabaseConnectionConfigIDRequest](../../models/operations/getdatabaseconnectionconfigidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetDatabaseConnectionConfigIDResponse](../../models/operations/getdatabaseconnectionconfigidresponse.md)**


## update

Update DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateDatabaseConnectionConfigIDRequest(
    database_connection_config=shared.DatabaseConnectionConfig(
        auth_type='quas',
        config_obj='et',
        connection_string='facilis',
        connection_timeout=229276,
        database_type=shared.DatabaseConnectionType(),
        description='autem',
        id='a08088d1-00ef-4ada-a00e-f0422eb2164c',
        request_timeout=975095,
        tags='molestias',
    ),
    id='ab8366c7-23ff-4da9-a06b-ee4825c1fc0e',
)

res = s.database_connection_config_id.update(req)

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.UpdateDatabaseConnectionConfigIDRequest](../../models/operations/updatedatabaseconnectionconfigidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.UpdateDatabaseConnectionConfigIDResponse](../../models/operations/updatedatabaseconnectionconfigidresponse.md)**

