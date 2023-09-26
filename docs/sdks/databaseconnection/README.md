# DatabaseConnection

### Available Operations

* [post](#post) - Create DatabaseConnectionConfig

## post

Create DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DatabaseConnectionConfig(
    auth_type='autem',
    config_obj='nobis',
    connection_string='quas',
    connection_timeout=829603,
    database_type=shared.DatabaseConnectionType(),
    description='nulla',
    id='6b144290-7474-4778-a7bd-466d28c10ab3',
    request_timeout=778696,
    tags='illum',
)

res = s.database_connection.post(req)

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DatabaseConnectionConfig](../../models/shared/databaseconnectionconfig.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PostDatabaseConnectionResponse](../../models/operations/postdatabaseconnectionresponse.md)**

