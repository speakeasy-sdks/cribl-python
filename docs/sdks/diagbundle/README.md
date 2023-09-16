# DiagBundle

### Available Operations

* [delete](#delete) - Remove diag bundle
* [get](#get) - Returns a diag bundle as a tar.gz archive
* [send](#send) - Send a diag bundle (tar.gz archive) to Cribl

## delete

Remove diag bundle

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.diag_bundle.delete(path='esse')

if res.remove_diag_response is not None:
    # handle response
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
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.diag_bundle.get()

if res.get_diag_bundle_200_application_tar_plus_gzip_binary_string is not None:
    # handle response
```


### Response

**[operations.GetDiagBundleResponse](../../models/operations/getdiagbundleresponse.md)**


## send

Send a diag bundle (tar.gz archive) to Cribl

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SendDiagBundle(
    include_metrics=False,
    max_include_jobs=910545,
    path='accusamus',
    rename_js=False,
    send_to_cribl=False,
)

res = s.diag_bundle.send(req)

if res.remove_diag_response is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.SendDiagBundle](../../models/shared/senddiagbundle.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.SendDiagBundleResponse](../../models/operations/senddiagbundleresponse.md)**

