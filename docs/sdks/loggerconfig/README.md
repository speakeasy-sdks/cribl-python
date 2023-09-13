# logger_config

### Available Operations

* [delete](#delete) - Delete LoggerConfig
* [get](#get) - Get LoggerConfig by ID
* [update](#update) - Update LoggerConfig

## delete

Delete LoggerConfig

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.logger_config.delete(id='alias')

if res.logger_config is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteLoggerConfigResponse](../../models/operations/deleteloggerconfigresponse.md)**


## get

Get LoggerConfig by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.logger_config.get(id='deleniti')

if res.logger_config is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetLoggerConfigResponse](../../models/operations/getloggerconfigresponse.md)**


## update

Update LoggerConfig

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.logger_config.update(id='earum', logger_config=shared.LoggerConfig(
    channels=[
        shared.LoggerEntry(
            can_delete=False,
            id='6f8c5f35-0d8c-4db5-a341-814301042181',
            level='dolor',
        ),
    ],
    default_redact_fields=[
        'fugiat',
    ],
    id='5208ece7-e253-4b66-8451-c6c6e205e16d',
    redact_fields=[
        'vero',
    ],
    redact_label='est',
))

if res.logger_config is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique ID                                                            |
| `logger_config`                                                      | [Optional[shared.LoggerConfig]](../../models/shared/loggerconfig.md) | :heavy_minus_sign:                                                   | LoggerConfig object to be updated                                    |


### Response

**[operations.UpdateLoggerConfigResponse](../../models/operations/updateloggerconfigresponse.md)**

