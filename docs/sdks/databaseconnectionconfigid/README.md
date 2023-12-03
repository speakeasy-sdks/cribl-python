# DatabaseConnectionConfigID
(*database_connection_config_id*)

### Available Operations

* [delete](#delete) - Delete DatabaseConnectionConfig
* [get](#get) - Get DatabaseConnectionConfig by ID
* [update](#update) - Update DatabaseConnectionConfig

## delete

Delete DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.database_connection_config_id.delete(id='string')

if res.database_connection_configs is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteDatabaseConnectionConfigIDResponse](../../models/operations/deletedatabaseconnectionconfigidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get DatabaseConnectionConfig by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.database_connection_config_id.get(id='string')

if res.database_connection_configs is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetDatabaseConnectionConfigIDResponse](../../models/operations/getdatabaseconnectionconfigidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.database_connection_config_id.update(id='string', database_connection_config=components.DatabaseConnectionConfig(
    auth_type='string',
    database_type=components.DatabaseConnectionType(),
    description='Synchronised 3rd generation matrix',
    id='<ID>',
))

if res.database_connection_configs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Unique ID                                                                                            |
| `database_connection_config`                                                                         | [Optional[components.DatabaseConnectionConfig]](../../models/components/databaseconnectionconfig.md) | :heavy_minus_sign:                                                                                   | DatabaseConnectionConfig object to be updated                                                        |


### Response

**[operations.UpdateDatabaseConnectionConfigIDResponse](../../models/operations/updatedatabaseconnectionconfigidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
