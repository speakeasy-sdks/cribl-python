# Pack
(*pack*)

### Available Operations

* [clone](#clone) - Clone Pack
* [export](#export) - Export Pack
* [install](#install) - Install Pack
* [uninstall](#uninstall) - Uninstall Pack from the system
* [upgrade](#upgrade) - Upgrade Pack
* [upload](#upload) - Upload Pack

## clone

Clone Pack

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.PackClone(
    dst_groups=[
        'West',
    ],
    packs=[
        'MTF',
    ],
    src_group='payment',
)

res = s.pack.clone(req)

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.PackClone](../../models/shared/packclone.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.ClonePackResponse](../../models/operations/clonepackresponse.md)**


## export

Export Pack

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.export(id='salmon', mode='hmph', filename='holistic')

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                 | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `id`                                                      | *str*                                                     | :heavy_check_mark:                                        | Pack name                                                 |
| `mode`                                                    | *str*                                                     | :heavy_check_mark:                                        | Export mode, one of "merge_safe", "merge", "default_only" |
| `filename`                                                | *Optional[str]*                                           | :heavy_minus_sign:                                        | Filename of the exported Pack                             |


### Response

**[operations.ExportPackResponse](../../models/operations/exportpackresponse.md)**


## install

Install Pack

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.CrudEntityBase(
    id='<ID>',
)

res = s.pack.install(req)

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.CrudEntityBase](../../models/shared/crudentitybase.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.InstallPackResponse](../../models/operations/installpackresponse.md)**


## uninstall

Uninstall Pack from the system

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.uninstall(id='male')

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Pack name          |


### Response

**[operations.UninstallPackResponse](../../models/operations/uninstallpackresponse.md)**


## upgrade

Upgrade Pack

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.upgrade(id='katal', minor='Producer', source='South', spec='online')

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | Pack name                                                   |
| `minor`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | body boolean optional Only upgrade to minor/patch versions  |
| `source`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | body string required Pack source                            |
| `spec`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | body string optional Specify a branch, tag or a semver spec |


### Response

**[operations.UpgradePackResponse](../../models/operations/upgradepackresponse.md)**


## upload

Upload Pack

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.upload(filename='Market')

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `filename`         | *Optional[str]*    | :heavy_minus_sign: | the file to upload |


### Response

**[operations.UploadPackResponse](../../models/operations/uploadpackresponse.md)**

