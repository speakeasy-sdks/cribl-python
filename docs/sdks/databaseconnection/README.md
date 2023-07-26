# database_connection

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
    auth_type='fuga',
    config_obj='laudantium',
    connection_string='incidunt',
    connection_timeout=97493,
    database_type=shared.DatabaseConnectionType(),
    description='rem',
    id='d162309f-b092-4992-9aef-b9f58c4d86e6',
    request_timeout=520761,
    tags='earum',
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

