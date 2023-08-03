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


res = s.logger_config.get(id='excepturi')

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


res = s.logger_config.update(id='a', logger_config=shared.LoggerConfig(
    channels=[
        shared.LoggerEntry(
            can_delete=False,
            id='8f0f816f-f347-47c1-be90-2c14125b0960',
            level='id',
        ),
        shared.LoggerEntry(
            can_delete=False,
            id='668151a4-72af-4923-8594-9f83f350cf87',
            level='aliquid',
        ),
        shared.LoggerEntry(
            can_delete=False,
            id='ffb901c6-ecbb-44e2-83cf-789ffafeda53',
            level='officiis',
        ),
        shared.LoggerEntry(
            can_delete=False,
            id='5ae6e0ac-184c-42b9-8247-c88373a40e19',
            level='dolore',
        ),
    ],
    default_redact_fields=[
        'maiores',
    ],
    id='32e55055-756f-45d5-ad0b-d0af2dfe13db',
    redact_fields=[
        'voluptatibus',
        'iure',
    ],
    redact_label='explicabo',
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

