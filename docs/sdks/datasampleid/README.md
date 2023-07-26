# data_sample_id

### Available Operations

* [delete](#delete) - Delete DataSample
* [get](#get) - Get DataSample by ID
* [update](#update) - Update DataSample

## delete

Delete DataSample

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.data_sample_id.delete('nemo')

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteDataSampleIDResponse](../../models/operations/deletedatasampleidresponse.md)**


## get

Get DataSample by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.data_sample_id.get('quos')

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetDataSampleIDResponse](../../models/operations/getdatasampleidresponse.md)**


## update

Update DataSample

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.data_sample_id.update('eius', {
    "ducimus": 'nesciunt',
})

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `id`                            | *str*                           | :heavy_check_mark:              | Unique ID                       |
| `request_body`                  | dict[str, *Any*]                | :heavy_minus_sign:              | DataSample object to be updated |


### Response

**[operations.UpdateDataSampleIDResponse](../../models/operations/updatedatasampleidresponse.md)**

