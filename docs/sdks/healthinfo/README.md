# HealthInfo
(*health_info*)

### Available Operations

* [get](#get) - Provides health info for REST server

## get

Provides health info for REST server

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.health_info.get()

if res.health_status is not None:
    # handle response
    pass
```


### Response

**[operations.GetHealthInfoResponse](../../models/operations/gethealthinforesponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.HealthStatus | 420                 | application/json    |
| errors.SDKError     | 4x-5xx              | */*                 |
