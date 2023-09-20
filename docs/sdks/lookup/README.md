# Lookup

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
    content='sequi',
    description='doloribus',
    id='ec9578a6-4584-4273-a841-8d162309fb09',
    size=178580,
    tags='occaecati',
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


res = s.lookup.delete(id='iste')

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


res = s.lookup.get(id='magni')

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


res = s.lookup.update(id='inventore', request_body=operations.UpdateLookupRequestBody2(
    content='accusamus',
    description='voluptatibus',
    id='b9f58c4d-86e6-48e4-be05-6013f59da757',
    size=667715,
    tags='quis',
))

if res.lookup_file is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `id`                            | *str*                           | :heavy_check_mark:              | Unique ID                       |
| `request_body`                  | *Optional[Any]*                 | :heavy_minus_sign:              | LookupFile object to be updated |


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


res = s.lookup.upload(filename='sint')

if res.lookup_file_info_response is not None:
    # handle response
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `filename`                                   | *Optional[str]*                              | :heavy_minus_sign:                           | query LookupFilenameSchema required Filename |


### Response

**[operations.UploadLookupResponse](../../models/operations/uploadlookupresponse.md)**

