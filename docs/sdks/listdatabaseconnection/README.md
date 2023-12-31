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


res = s.list_database_connection.get('sed')

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `database_type`             | *Optional[str]*             | :heavy_minus_sign:          | type of database connection |


### Response

**[operations.GetListDatabaseConnectionResponse](../../models/operations/getlistdatabaseconnectionresponse.md)**

