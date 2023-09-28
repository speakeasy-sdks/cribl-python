# Profiler
(*profiler*)

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
    create_time=185518,
    id='b895c537-c645-44ef-b0b3-4896c3ca5acf',
    size=735894,
    worker_id='vero',
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


res = s.profiler.delete(id='odit')

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


res = s.profiler.get(id='repellat')

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


res = s.profiler.update(id='pariatur', profiler_item=shared.ProfilerItem(
    create_time=362888,
    id='70757792-9177-4dea-8646-ecb573409e3e',
    size=741232,
    worker_id='dicta',
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

