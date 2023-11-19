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
from cribl.models import operations

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get DataSample by ID

### Example Usage

```python
import cribl
from cribl.models import operations

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update DataSample

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.data_sample_id.update(id='string', data_sample=components.DataSample(
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

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique ID                                                                |
| `data_sample`                                                            | [Optional[components.DataSample]](../../models/components/datasample.md) | :heavy_minus_sign:                                                       | DataSample object to be updated                                          |


### Response

**[operations.UpdateDataSampleIDResponse](../../models/operations/updatedatasampleidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
