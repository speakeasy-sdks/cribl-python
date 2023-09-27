# Lookup
(*lookup*)

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
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = []

res = s.lookup.create(req)

if res.lookup_files is not None:
    # handle response
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `request`                                    | [Union[]](../../models/shared/lookupfile.md) | :heavy_check_mark:                           | The request object to use for the request.   |


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


res = s.lookup.delete(id='ipsam')

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.lookup.get(id='culpa')

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.lookup.update(id='dolor', lookup_file=[])

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | Unique ID                                              |
| `lookup_file`                                          | [Optional[Union[]]](../../models/shared/lookupfile.md) | :heavy_minus_sign:                                     | LookupFile object to be updated                        |


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


res = s.lookup.upload(filename='aliquam')

if res.lookup_file_info_response is not None:
    # handle response
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `filename`                                   | *Optional[str]*                              | :heavy_minus_sign:                           | query LookupFilenameSchema required Filename |


### Response

**[operations.UploadLookupResponse](../../models/operations/uploadlookupresponse.md)**

