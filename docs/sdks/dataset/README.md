# dataset

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DatasetProviderType(
    description='nam',
    id=shared.ProviderType.QUICKSORT,
    locality=shared.OriginConfig(
        filter_expression='iusto',
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset.delete(id='voluptate')

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset.get(id='sequi')

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset.update(id='dignissimos', dataset_provider_type=shared.DatasetProviderType(
    description='neque',
    id=shared.ProviderType.INVALID,
    locality=shared.OriginConfig(
        filter_expression='deleniti',
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

