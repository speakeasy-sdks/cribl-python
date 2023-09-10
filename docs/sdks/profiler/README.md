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
    create_time=350325,
    id='7411faf4-b754-44e4-b2e8-02857a5b4046',
    size=199529,
    worker_id='mollitia',
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


res = s.profiler.delete(id='dignissimos')

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


res = s.profiler.get(id='fugiat')

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


res = s.profiler.update(id='nostrum', profiler_item=shared.ProfilerItem(
    create_time=475325,
    id='5f1400e7-64ad-4733-8ec1-b781b36a0808',
    size=511222,
    worker_id='repellendus',
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

