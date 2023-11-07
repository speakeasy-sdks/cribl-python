# DiagBundle
(*.diag_bundle*)

### Available Operations

* [delete](#delete) - Remove diag bundle
* [get](#get) - Returns a diag bundle as a tar.gz archive
* [send](#send) - Send a diag bundle (tar.gz archive) to Cribl

## delete

Remove diag bundle

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.diag_bundle.delete(path='string')

if res.remove_diag_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `path`             | *str*              | :heavy_check_mark: | Diag bundle path   |


### Response

**[operations.DeleteDiagBundleResponse](../../models/operations/deletediagbundleresponse.md)**


## get

Returns a diag bundle as a tar.gz archive

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.diag_bundle.get()

if res.stream is not None:
    # handle response
    pass
```


### Response

**[operations.GetDiagBundleResponse](../../models/operations/getdiagbundleresponse.md)**


## send

Send a diag bundle (tar.gz archive) to Cribl

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.SendDiagBundle()

res = s.diag_bundle.send(req)

if res.remove_diag_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.SendDiagBundle](../../models/shared/senddiagbundle.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.SendDiagBundleResponse](../../models/operations/senddiagbundleresponse.md)**

