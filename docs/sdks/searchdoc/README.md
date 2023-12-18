# SearchDoc
(*search_doc*)

### Available Operations

* [get](#get) - Get Search documentation

## get

Get Search documentation

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_doc.get()

if res.res is not None:
    # handle response
    pass
```


### Response

**[operations.GetSearchDocResponse](../../models/operations/getsearchdocresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
