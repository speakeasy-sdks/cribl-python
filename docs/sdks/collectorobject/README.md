# CollectorObject
(*collector_object*)

### Available Operations

* [get](#get) - Get a list of Collector objects

## get

Get a list of Collector objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.collector_object.get()

if res.collectors is not None:
    # handle response
    pass
```


### Response

**[operations.GetCollectorObjectResponse](../../models/operations/getcollectorobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
