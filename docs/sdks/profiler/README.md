# profiler

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
    create_time=218783,
    id='c8db0340-8d6d-4364-bfd4-55906d1263d4',
    size=523109,
    worker_id='officiis',
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


res = s.profiler.delete(id='omnis')

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


res = s.profiler.get(id='neque')

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


res = s.profiler.update(id='corporis', profiler_item=shared.ProfilerItem(
    create_time=797527,
    id='2c9e81f3-0be3-4e43-a02d-721657650664',
    size=94122,
    worker_id='rem',
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

