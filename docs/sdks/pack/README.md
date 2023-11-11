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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.PackClone(
    dst_groups=[
        'string',
    ],
    packs=[
        'string',
    ],
    src_group='string',
)

res = s.pack.clone(req)

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.PackClone](../../models/components/packclone.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.ClonePackResponse](../../models/operations/clonepackresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## export

Export Pack

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.export(id='string', mode='string', filename='string')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## install

Install Pack

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.CrudEntityBase(
    id='<ID>',
)

res = s.pack.install(req)

if res.pack_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.CrudEntityBase](../../models/components/crudentitybase.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.InstallPackResponse](../../models/operations/installpackresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## uninstall

Uninstall Pack from the system

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.uninstall(id='string')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## upgrade

Upgrade Pack

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.upgrade(id='string', minor='string', source='string', spec='string')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## upload

Upload Pack

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pack.upload(filename='string')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
