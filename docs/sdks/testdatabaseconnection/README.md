# test_database_connection

### Available Operations

* [post](#post) - Test a database connection given a type and connectionString

## post

Test a database connection given a type and connectionString

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DatabaseConnectionTest(
    auth_type='quod',
    config_obj='voluptatibus',
    connection_string='voluptas',
    connection_timeout=247767,
    database_type='ullam',
    text_secret='laborum',
)

res = s.test_database_connection.post(req)

if res.database_connection_test_results is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.DatabaseConnectionTest](../../models/shared/databaseconnectiontest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PostTestDatabaseConnectionResponse](../../models/operations/posttestdatabaseconnectionresponse.md)**

