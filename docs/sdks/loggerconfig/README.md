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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logger_config.delete(id='string')

if res.logger_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteLoggerConfigResponse](../../models/operations/deleteloggerconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get LoggerConfig by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logger_config.get(id='string')

if res.logger_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetLoggerConfigResponse](../../models/operations/getloggerconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update LoggerConfig

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logger_config.update(id='string', logger_config=components.LoggerConfig(
    channels=[
        components.LoggerEntry(
            id='<ID>',
            level='string',
        ),
    ],
    default_redact_fields=[
        'string',
    ],
    id='<ID>',
    redact_fields=[
        'string',
    ],
    redact_label='string',
))

if res.logger_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique ID                                                                    |
| `logger_config`                                                              | [Optional[components.LoggerConfig]](../../models/components/loggerconfig.md) | :heavy_minus_sign:                                                           | LoggerConfig object to be updated                                            |


### Response

**[operations.UpdateLoggerConfigResponse](../../models/operations/updateloggerconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
