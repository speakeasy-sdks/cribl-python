# ListDatabaseConnection
(*list_database_connection*)

### Available Operations

* [get](#get) - Get a list of DatabaseConnection objects

## get

Get a list of DatabaseConnection objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_database_connection.get(database_type='<value>')

if res.database_connection_configs is not None:
    # handle response
    pass

```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `database_type`             | *Optional[str]*             | :heavy_minus_sign:          | type of database connection |


### Response

**[operations.GetListDatabaseConnectionResponse](../../models/operations/getlistdatabaseconnectionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
