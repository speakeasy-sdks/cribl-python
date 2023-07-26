# pack

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.PackClone(
    dest='dolorem',
    dst_groups=[
        'ipsa',
    ],
    force=False,
    packs=[
        'repellendus',
        'soluta',
        'aut',
    ],
    src_group='ullam',
)

res = s.pack.clone(req)

if res.pack_infos is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ExportPackRequest(
    filename='amet',
    id='6d9e75ca-006f-4539-ac11-a25a8bf92f97',
    mode='dolore',
)

res = s.pack.export(req)

if res.pack_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ExportPackRequest](../../models/operations/exportpackrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ExportPackResponse](../../models/operations/exportpackresponse.md)**


## install

Install Pack

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.CrudEntityBase(
    id='28ad9a9f-8bf8-4221-9253-59d98387f7a7',
)

res = s.pack.install(req)

if res.pack_infos is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UninstallPackRequest(
    id='9cd72cd2-484d-4a21-b29f-2ac41ef5725f',
)

res = s.pack.uninstall(req)

if res.pack_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UninstallPackRequest](../../models/operations/uninstallpackrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UninstallPackResponse](../../models/operations/uninstallpackresponse.md)**


## upgrade

Upgrade Pack

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpgradePackRequest(
    id='1169ac1e-41d8-4a23-823e-34f2dfa4a197',
    minor='a',
    source='iure',
    spec='nulla',
)

res = s.pack.upgrade(req)

if res.pack_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpgradePackRequest](../../models/operations/upgradepackrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpgradePackResponse](../../models/operations/upgradepackresponse.md)**


## upload

Upload Pack

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UploadPackRequest(
    filename='recusandae',
)

res = s.pack.upload(req)

if res.pack_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UploadPackRequest](../../models/operations/uploadpackrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UploadPackResponse](../../models/operations/uploadpackresponse.md)**

