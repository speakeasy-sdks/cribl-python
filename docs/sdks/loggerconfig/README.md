# LoggerConfig
(*logger_config*)

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


res = s.logger_config.delete(id='ipsa')

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


res = s.logger_config.get(id='laborum')

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


res = s.logger_config.update(id='sunt', logger_config=shared.LoggerConfig(
    channels=[
        shared.LoggerEntry(
            can_delete=False,
            id='5db6a660-659a-41ad-aaab-5851d6c645b0',
            level='molestias',
        ),
    ],
    default_redact_fields=[
        'cum',
    ],
    id='61891baa-0fe1-4ade-808e-6f8c5f350d8c',
    redact_fields=[
        'quibusdam',
    ],
    redact_label='nam',
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

