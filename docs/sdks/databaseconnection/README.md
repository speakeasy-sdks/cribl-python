# DatabaseConnection
(*database_connection*)

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
    auth_type='Producer base',
    config_obj='protocol off beside',
    connection_string='Arizona synthesizing',
    connection_timeout=767148,
    database_type=shared.DatabaseConnectionType(),
    description='Fundamental grid-enabled emulation',
    id='<ID>',
    request_timeout=15395,
    tags='Southeast array',
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

