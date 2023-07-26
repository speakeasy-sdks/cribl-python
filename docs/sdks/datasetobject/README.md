# dataset_object

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

req = 'fuga'

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

req = operations.DeleteDatasetObjectRequest(
    id='51262438-35bb-4c05-a23a-45cefc5fde10',
)

res = s.dataset_object.delete(req)

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteDatasetObjectRequest](../../models/operations/deletedatasetobjectrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


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

req = operations.GetDatasetObjectRequest(
    id='a0ce2169-e510-4019-86dc-5e34762799bf',
)

res = s.dataset_object.get(req)

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetDatasetObjectRequest](../../models/operations/getdatasetobjectrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


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

req = operations.UpdateDatasetObjectRequest(
    request_body='facilis',
    id='be6949fb-2bb4-4eca-a6c3-d5db3adebd5d',
)

res = s.dataset_object.update(req)

if res.dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateDatasetObjectRequest](../../models/operations/updatedatasetobjectrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.UpdateDatasetObjectResponse](../../models/operations/updatedatasetobjectresponse.md)**

