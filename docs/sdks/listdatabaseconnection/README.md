# list_database_connection

### Available Operations

* [get](#get) - Get a list of DatabaseConnection objects

## get

Get a list of DatabaseConnection objects

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetListDatabaseConnectionRequest(
    database_type='similique',
)

res = s.list_database_connection.get(req)

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetListDatabaseConnectionRequest](../../models/operations/getlistdatabaseconnectionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetListDatabaseConnectionResponse](../../models/operations/getlistdatabaseconnectionresponse.md)**

