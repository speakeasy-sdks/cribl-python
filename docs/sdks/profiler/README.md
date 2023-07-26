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
    create_time=78158,
    id='31911296-4664-45c1-981f-29042f569b7a',
    size=972398,
    worker_id='a',
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

req = operations.DeleteProfilerRequest(
    id='0ea2216c-be07-41bc-963e-279a3b084da9',
)

res = s.profiler.delete(req)

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteProfilerRequest](../../models/operations/deleteprofilerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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

req = operations.GetProfilerRequest(
    id='9257d04f-4084-47a7-82d8-4496cbdeecf6',
)

res = s.profiler.get(req)

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetProfilerRequest](../../models/operations/getprofilerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


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

req = operations.UpdateProfilerRequest(
    profiler_item=shared.ProfilerItem(
        create_time=736126,
        id='99bc6356-2ebf-4df5-9c29-4c060b06a128',
        size=476770,
        worker_id='voluptate',
    ),
    id='64eef6d0-c6d6-4ed9-873d-d634571509a8',
)

res = s.profiler.update(req)

if res.profiler_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateProfilerRequest](../../models/operations/updateprofilerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateProfilerResponse](../../models/operations/updateprofilerresponse.md)**

