# logger_configs

### Available Operations

* [get](#get) - Get a list of LoggerConfig objects

## get

Get a list of LoggerConfig objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.logger_configs.get()

if res.logger_configs is not None:
    # handle response
```


### Response

**[operations.GetLoggerConfigsResponse](../../models/operations/getloggerconfigsresponse.md)**

