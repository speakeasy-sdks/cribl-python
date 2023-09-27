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
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.database_connection_config_id.delete(id='quo')

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteDatabaseConnectionConfigIDResponse](../../models/operations/deletedatabaseconnectionconfigidresponse.md)**


## get

Get DatabaseConnectionConfig by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.database_connection_config_id.get(id='fuga')

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetDatabaseConnectionConfigIDResponse](../../models/operations/getdatabaseconnectionconfigidresponse.md)**


## update

Update DatabaseConnectionConfig

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.database_connection_config_id.update(id='eius', database_connection_config=shared.DatabaseConnectionConfig(
    auth_type='eos',
    config_obj='voluptas',
    connection_string='ab',
    connection_timeout=587600,
    database_type=shared.DatabaseConnectionType(),
    description='consequatur',
    id='4e523c7e-0bc7-4178-a479-6f2a70c68828',
    request_timeout=143829,
    tags='fuga',
))

if res.database_connection_configs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `id`                                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | Unique ID                                                                                    |
| `database_connection_config`                                                                 | [Optional[shared.DatabaseConnectionConfig]](../../models/shared/databaseconnectionconfig.md) | :heavy_minus_sign:                                                                           | DatabaseConnectionConfig object to be updated                                                |


### Response

**[operations.UpdateDatabaseConnectionConfigIDResponse](../../models/operations/updatedatabaseconnectionconfigidresponse.md)**

