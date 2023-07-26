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
    description='architecto',
    id=shared.ProviderType.MM_HEAP,
    locality=shared.OriginConfig(
        filter_expression='enim',
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

req = operations.DeleteDatasetProviderTypeRequest(
    id='c80bff91-8544-4ec4-adef-cce8f1977773',
)

res = s.dataset.delete(req)

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteDatasetProviderTypeRequest](../../models/operations/deletedatasetprovidertyperequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


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

req = operations.GetDatasetProviderTypeRequest(
    id='e63562a7-b408-4f05-a3d4-8fdaf313a1f5',
)

res = s.dataset.get(req)

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetDatasetProviderTypeRequest](../../models/operations/getdatasetprovidertyperequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


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

req = operations.UpdateDatasetProviderTypeRequest(
    dataset_provider_type=shared.DatasetProviderType(
        description='doloribus',
        id=shared.ProviderType.INVALID,
        locality=shared.OriginConfig(
            filter_expression='unde',
            origin=shared.DatasetOrigin(),
        ),
    ),
    id='4259c0b3-6f25-4ea9-84f3-b756c11f6c37',
)

res = s.dataset.update(req)

if res.dataset_provider_type is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateDatasetProviderTypeRequest](../../models/operations/updatedatasetprovidertyperequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.UpdateDatasetProviderTypeResponse](../../models/operations/updatedatasetprovidertyperesponse.md)**

