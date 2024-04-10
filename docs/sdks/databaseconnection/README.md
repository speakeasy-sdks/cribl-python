# DatabaseConnection
(*database_connection*)

### Available Operations

* [post](#post) - Create DatabaseConnectionConfig

## post

Create DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.DatabaseConnectionConfig(
    auth_type='<value>',
    description='Monitored needs-based parallelism',
    id='<id>',
)

res = s.database_connection.post(req)

if res.database_connection_configs is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.DatabaseConnectionConfig](../../models/components/databaseconnectionconfig.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PostDatabaseConnectionResponse](../../models/operations/postdatabaseconnectionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
