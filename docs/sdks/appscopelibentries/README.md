# AppscopeLibEntries
(*appscope_lib_entries*)

### Available Operations

* [get](#get) - Get a list of AppscopeLibEntry objects

## get

Get a list of AppscopeLibEntry objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.appscope_lib_entries.get()

if res.app_scope_lib_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetAppscopeLibEntriesResponse](../../models/operations/getappscopelibentriesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |
