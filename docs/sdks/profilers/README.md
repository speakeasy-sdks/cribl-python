# Profilers
(*profilers*)

### Available Operations

* [get](#get) - Get a list of ProfilerItem objects

## get

Get a list of ProfilerItem objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.profilers.get()

if res.profiler_items is not None:
    # handle response
    pass

```


### Response

**[operations.GetProfilersResponse](../../models/operations/getprofilersresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
