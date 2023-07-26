# lookup

### Available Operations

* [create](#create) - Create LookupFile
* [delete](#delete) - Delete LookupFile
* [get](#get) - Get LookupFile by ID
* [update](#update) - Update LookupFile
* [upload](#upload) - Upload LookupFile

## create

Create LookupFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateLookupRequestBody2(
    content='repellendus',
    description='delectus',
    id='1ad837ae-80c1-4c19-895b-a998678fa3f6',
    size=575634,
    tags='autem',
)

res = s.lookup.create(req)

if res.lookup_files is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateLookupResponse](../../models/operations/createlookupresponse.md)**


## delete

Delete LookupFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteLookupRequest(
    id='991af388-ce03-4614-848c-7977a0ef2f53',
)

res = s.lookup.delete(req)

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteLookupRequest](../../models/operations/deletelookuprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteLookupResponse](../../models/operations/deletelookupresponse.md)**


## get

Get LookupFile by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetLookupRequest(
    id='6028efee-f934-4152-ad7e-253f4c157dea',
)

res = s.lookup.get(req)

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetLookupRequest](../../models/operations/getlookuprequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetLookupResponse](../../models/operations/getlookupresponse.md)**


## update

Update LookupFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateLookupRequest(
    request_body=operations.UpdateLookupRequestBody2(
        content='in',
        description='illo',
        id='70f445ac-cf66-47aa-b9bb-ad185fe431d6',
        size=696324,
        tags='delectus',
    ),
    id='5c838fbb-8c20-4cb6-bfc4-b425e99e6234',
)

res = s.lookup.update(req)

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateLookupRequest](../../models/operations/updatelookuprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateLookupResponse](../../models/operations/updatelookupresponse.md)**


## upload

Upload LookupFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UploadLookupRequest(
    filename='porro',
)

res = s.lookup.upload(req)

if res.lookup_file_info_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UploadLookupRequest](../../models/operations/uploadlookuprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UploadLookupResponse](../../models/operations/uploadlookupresponse.md)**

