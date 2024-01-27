# ObjectFunction
(*object_function*)

### Available Operations

* [get](#get) - Get a list of Function objects

## get

Get a list of Function objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.object_function.get()

if res.functions is not None:
    # handle response
    pass
```


### Response

**[operations.GetObjectFunctionResponse](../../models/operations/getobjectfunctionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
