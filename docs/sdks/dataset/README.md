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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.DatasetProviderType(
    id=components.ProviderType.QUICKSORT,
    locality=components.OriginConfig(
        origin=components.DatasetOrigin(),
    ),
)

res = s.dataset.create(req)

if res.dataset_provider_type is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.DatasetProviderType](../../models/components/datasetprovidertype.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateDatasetProviderTypeResponse](../../models/operations/createdatasetprovidertyperesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete DatasetProviderType

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.delete(id='string')

if res.dataset_provider_type is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteDatasetProviderTypeResponse](../../models/operations/deletedatasetprovidertyperesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get DatasetProviderType by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.get(id='string')

if res.dataset_provider_type is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetDatasetProviderTypeResponse](../../models/operations/getdatasetprovidertyperesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update DatasetProviderType

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.update(id='string', dataset_provider_type=components.DatasetProviderType(
    id=components.ProviderType.INVALID,
    locality=components.OriginConfig(
        origin=components.DatasetOrigin(),
    ),
))

if res.dataset_provider_type is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | Unique ID                                                                                  |
| `dataset_provider_type`                                                                    | [Optional[components.DatasetProviderType]](../../models/components/datasetprovidertype.md) | :heavy_minus_sign:                                                                         | DatasetProviderType object to be updated                                                   |


### Response

**[operations.UpdateDatasetProviderTypeResponse](../../models/operations/updatedatasetprovidertyperesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
