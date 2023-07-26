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

req = operations.DeleteDataSampleIDRequest(
    id='319c177d-525f-477b-914e-eb52ff785fc3',
)

res = s.data_sample_id.delete(req)

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteDataSampleIDRequest](../../models/operations/deletedatasampleidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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

req = operations.GetDataSampleIDRequest(
    id='7814d4c9-8e0c-42bb-89eb-75dad636c600',
)

res = s.data_sample_id.get(req)

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetDataSampleIDRequest](../../models/operations/getdatasampleidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


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

req = operations.UpdateDataSampleIDRequest(
    request_body={
        "quae": 'amet',
        "illum": 'praesentium',
    },
    id='bb31180f-739a-4e9e-857e-b809e2810331',
)

res = s.data_sample_id.update(req)

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateDataSampleIDRequest](../../models/operations/updatedatasampleidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateDataSampleIDResponse](../../models/operations/updatedatasampleidresponse.md)**

