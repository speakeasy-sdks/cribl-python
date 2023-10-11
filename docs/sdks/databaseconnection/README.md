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
    bearer_auth="",
)

req = shared.DatabaseConnectionConfig(
    auth_type='Producer base',
    database_type=shared.DatabaseConnectionType(),
    description='Synergized incremental alliance',
    id='<ID>',
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

