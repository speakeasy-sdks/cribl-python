# DataSampleID
(*data_sample_id*)

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
    bearer_auth="",
)


res = s.data_sample_id.delete(id='string')

if res.data_samples is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.data_sample_id.get(id='string')

if res.data_samples is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.data_sample_id.update(id='string', data_sample=shared.DataSample(
    additional_properties={
        "key": 'string',
    },
    id='<ID>',
    sample_name='string',
))

if res.data_samples is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Unique ID                                                        |
| `data_sample`                                                    | [Optional[shared.DataSample]](../../models/shared/datasample.md) | :heavy_minus_sign:                                               | DataSample object to be updated                                  |


### Response

**[operations.UpdateDataSampleIDResponse](../../models/operations/updatedatasampleidresponse.md)**

