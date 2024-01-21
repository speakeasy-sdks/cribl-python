# ExistingDiagBundles
(*existing_diag_bundles*)

### Available Operations

* [get](#get) - Get list of existing diag bundles

## get

Get list of existing diag bundles

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.existing_diag_bundles.get()

if res.existing_diag is not None:
    # handle response
    pass
```


### Response

**[operations.GetExistingDiagBundlesResponse](../../models/operations/getexistingdiagbundlesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
