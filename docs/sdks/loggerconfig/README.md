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

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logger_config.delete(id='<value>')

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
| errors.SDKError  | 4xx-5xx          | */*              |

## get

Get LoggerConfig by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logger_config.get(id='<value>')

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
| errors.SDKError  | 4xx-5xx          | */*              |

## update

Update LoggerConfig

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.logger_config.update(id='<value>', logger_config=components.LoggerConfig(
    channels=[
        components.LoggerEntry(
            id='<id>',
            level='<value>',
        ),
    ],
    id='<id>',
    redact_fields=[
        '<value>',
    ],
    redact_label='<value>',
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
| errors.SDKError  | 4xx-5xx          | */*              |
