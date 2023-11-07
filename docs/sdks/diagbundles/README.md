# DiagBundles
(*.diag_bundles*)

### Available Operations

* [get](#get) - Get list of existing diag bundles

## get

Get list of existing diag bundles

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.diag_bundles.get()

if res.stream is not None:
    # handle response
    pass
```


### Response

**[operations.GetDiagBundlesResponse](../../models/operations/getdiagbundlesresponse.md)**

