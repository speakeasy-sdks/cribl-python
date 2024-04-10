# ListGlobalVariable
(*list_global_variable*)

### Available Operations

* [get](#get) - Get a list of Global Variable objects

## get

Get a list of Global Variable objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_global_variable.get()

if res.global_vars is not None:
    # handle response
    pass

```


### Response

**[operations.GetListGlobalVariableResponse](../../models/operations/getlistglobalvariableresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
