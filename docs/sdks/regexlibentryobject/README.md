# RegexLibEntryObject
(*regex_lib_entry_object*)

### Available Operations

* [get](#get) - Get a list of RegexLibEntry objects

## get

Get a list of RegexLibEntry objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.regex_lib_entry_object.get()

if res.regex_lib_entries is not None:
    # handle response
    pass

```


### Response

**[operations.GetRegexLibEntryObjectResponse](../../models/operations/getregexlibentryobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
