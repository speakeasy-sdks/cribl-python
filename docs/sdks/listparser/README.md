# ListParser
(*list_parser*)

### Available Operations

* [get](#get) - Get a list of Parser objects

## get

Get a list of Parser objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_parser.get()

if res.parser_lib_entries is not None:
    # handle response
    pass

```


### Response

**[operations.GetListParserResponse](../../models/operations/getlistparserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
