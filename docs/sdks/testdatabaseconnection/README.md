# TestDatabaseConnection
(*test_database_connection*)

### Available Operations

* [post](#post) - Test a database connection given a type and connectionString

## post

Test a database connection given a type and connectionString

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.DatabaseConnectionTest(
    auth_type='<value>',
    database_type='<value>',
)

res = s.test_database_connection.post(req)

if res.database_connection_test_results is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.DatabaseConnectionTest](../../models/components/databaseconnectiontest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PostTestDatabaseConnectionResponse](../../models/operations/posttestdatabaseconnectionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
