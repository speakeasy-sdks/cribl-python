# LoggerConfigs
(*.logger_configs*)

### Available Operations

* [get](#get) - Get a list of LoggerConfig objects

## get

Get a list of LoggerConfig objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.logger_configs.get()

if res.logger_configs is not None:
    # handle response
    pass
```


### Response

**[operations.GetLoggerConfigsResponse](../../models/operations/getloggerconfigsresponse.md)**

