# DiagBundles
(*diag_bundles*)

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


res = s.diag_bundles.get()

if res.stream is not None:
    # handle response
    pass
```


### Response

**[operations.GetDiagBundlesResponse](../../models/operations/getdiagbundlesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400,404          | application/json |
| errors.SDKError  | 400-600          | */*              |
