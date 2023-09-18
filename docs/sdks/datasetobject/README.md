# DatasetObject

### Available Operations

* [create](#create) - Create Dataset
* [delete](#delete) - Delete Dataset
* [get](#get) - Get Dataset by ID
* [update](#update) - Update Dataset

## create

Create Dataset

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = 'ratione'

res = s.dataset_object.create(req)

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateDatasetObjectResponse](../../models/operations/createdatasetobjectresponse.md)**


## delete

Delete Dataset

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset_object.delete(id='explicabo')

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteDatasetObjectResponse](../../models/operations/deletedatasetobjectresponse.md)**


## get

Get Dataset by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset_object.get(id='saepe')

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetDatasetObjectResponse](../../models/operations/getdatasetobjectresponse.md)**


## update

Update Dataset

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset_object.update(id='occaecati', request_body='atque')

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `id`                         | *str*                        | :heavy_check_mark:           | Unique ID                    |
| `request_body`               | *Optional[Any]*              | :heavy_minus_sign:           | Dataset object to be updated |


### Response

**[operations.UpdateDatasetObjectResponse](../../models/operations/updatedatasetobjectresponse.md)**

