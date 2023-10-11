# Dataset
(*dataset*)

### Available Operations

* [create](#create) - Create DatasetProviderType
* [delete](#delete) - Delete DatasetProviderType
* [get](#get) - Get DatasetProviderType by ID
* [update](#update) - Update DatasetProviderType

## create

Create DatasetProviderType

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.DatasetProviderType(
    id=shared.ProviderType.QUICKSORT,
    locality=shared.OriginConfig(
        origin=shared.DatasetOrigin(),
    ),
)

res = s.dataset.create(req)

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.DatasetProviderType](../../models/shared/datasetprovidertype.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateDatasetProviderTypeResponse](../../models/operations/createdatasetprovidertyperesponse.md)**


## delete

Delete DatasetProviderType

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.dataset.delete(id='program')

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteDatasetProviderTypeResponse](../../models/operations/deletedatasetprovidertyperesponse.md)**


## get

Get DatasetProviderType by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.dataset.get(id='female')

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetDatasetProviderTypeResponse](../../models/operations/getdatasetprovidertyperesponse.md)**


## update

Update DatasetProviderType

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.dataset.update(id='Van', dataset_provider_type=shared.DatasetProviderType(
    id=shared.ProviderType.MM_HEAP,
    locality=shared.OriginConfig(
        origin=shared.DatasetOrigin(),
    ),
))

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | Unique ID                                                                          |
| `dataset_provider_type`                                                            | [Optional[shared.DatasetProviderType]](../../models/shared/datasetprovidertype.md) | :heavy_minus_sign:                                                                 | DatasetProviderType object to be updated                                           |


### Response

**[operations.UpdateDatasetProviderTypeResponse](../../models/operations/updatedatasetprovidertyperesponse.md)**

