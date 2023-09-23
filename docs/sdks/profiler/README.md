# Profiler

### Available Operations

* [create](#create) - Create ProfilerItem
* [delete](#delete) - Delete ProfilerItem
* [get](#get) - Get ProfilerItem by ID
* [update](#update) - Update ProfilerItem

## create

Create ProfilerItem

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ProfilerItem(
    create_time=97676,
    id='180f739a-e9e0-457e-b809-e2810331f398',
    size=107472,
    worker_id='at',
)

res = s.profiler.create(req)

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.ProfilerItem](../../models/shared/profileritem.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateProfilerResponse](../../models/operations/createprofilerresponse.md)**


## delete

Delete ProfilerItem

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.profiler.delete(id='labore')

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteProfilerResponse](../../models/operations/deleteprofilerresponse.md)**


## get

Get ProfilerItem by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.profiler.get(id='minus')

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetProfilerResponse](../../models/operations/getprofilerresponse.md)**


## update

Update ProfilerItem

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.profiler.update(id='esse', profiler_item=shared.ProfilerItem(
    create_time=32356,
    id='0b607f3c-93c7-43b9-9a3f-2ceda7e23f22',
    size=350325,
    worker_id='nihil',
))

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique ID                                                            |
| `profiler_item`                                                      | [Optional[shared.ProfilerItem]](../../models/shared/profileritem.md) | :heavy_minus_sign:                                                   | ProfilerItem object to be updated                                    |


### Response

**[operations.UpdateProfilerResponse](../../models/operations/updateprofilerresponse.md)**

