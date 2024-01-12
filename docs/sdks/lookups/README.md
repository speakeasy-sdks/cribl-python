# Lookups
(*lookups*)

### Available Operations

* [get](#get) - Get a list of LookupFile objects

## get

Get a list of LookupFile objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.lookups.get()

if res.lookup_files is not None:
    # handle response
    pass
```


### Response

**[operations.GetLookupsResponse](../../models/operations/getlookupsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
