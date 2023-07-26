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

req = operations.DeleteLoggerConfigRequest(
    id='2f745339-94d7-48de-bb6e-9389f5abb7f6',
)

res = s.logger_config.delete(req)

if res.logger_config is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteLoggerConfigRequest](../../models/operations/deleteloggerconfigrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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

req = operations.GetLoggerConfigRequest(
    id='62550a28-382a-4c48-bafd-2315bba65016',
)

res = s.logger_config.get(req)

if res.logger_config is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetLoggerConfigRequest](../../models/operations/getloggerconfigrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


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

req = operations.UpdateLoggerConfigRequest(
    logger_config=shared.LoggerConfig(
        channels=[
            shared.LoggerEntry(
                can_delete=False,
                id='e06f5bf6-ae59-41bc-8bde-f3612b63c205',
                level='a',
            ),
            shared.LoggerEntry(
                can_delete=False,
                id='da840774-a68a-49a3-9d08-6b6f66fef020',
                level='voluptates',
            ),
        ],
        default_redact_fields=[
            'maiores',
            'quaerat',
            'numquam',
        ],
        id='3b4257b9-92c8-4dbd-a6a6-1efa2198258f',
        redact_fields=[
            'aut',
            'similique',
            'iste',
            'eveniet',
        ],
        redact_label='nam',
    ),
    id='a47f7d3e-f049-4640-96a1-831c87adf596',
)

res = s.logger_config.update(req)

if res.logger_config is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateLoggerConfigRequest](../../models/operations/updateloggerconfigrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateLoggerConfigResponse](../../models/operations/updateloggerconfigresponse.md)**

