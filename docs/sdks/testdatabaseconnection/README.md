# TestDatabaseConnection
(*.test_database_connection*)

### Available Operations

* [post](#post) - Test a database connection given a type and connectionString

## post

Test a database connection given a type and connectionString

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.DatabaseConnectionTest(
    auth_type='string',
    database_type='string',
)

res = s.test_database_connection.post(req)

if res.database_connection_test_results is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DatabaseConnectionTest](../../models/shared/databaseconnectiontest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PostTestDatabaseConnectionResponse](../../models/operations/posttestdatabaseconnectionresponse.md)**

