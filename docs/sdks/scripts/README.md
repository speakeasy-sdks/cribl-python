# Scripts
(*scripts*)

### Available Operations

* [get](#get) - Get a list of Script objects

## get

Get a list of Script objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.scripts.get()

if res.script_lib_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetScriptsResponse](../../models/operations/getscriptsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
