# Schemas
(*schemas*)

### Available Operations

* [get](#get) - Get a list of Schema objects

## get

Get a list of Schema objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.schemas.get()

if res.schema_lib_entries is not None:
    # handle response
    pass

```


### Response

**[operations.GetSchemasResponse](../../models/operations/getschemasresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
