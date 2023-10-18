# SavedJobs
(*saved_jobs*)

### Available Operations

* [create](#create) - Create SavedJob
* [get](#get) - Get a list of SavedJob objects

## create

Create SavedJob

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.SavedJobExecutor(
    executor=shared.SavedJobExecutorExecutor(
        conf=shared.SavedJobExecutorExecutorExecutorSpecificSettings(),
        type='bluetooth',
    ),
    remove_fields=[
        'Extended',
    ],
    schedule=shared.SavedJobExecutorSchedule(
        run=shared.SavedJobExecutorScheduleRunSettings(),
    ),
    streamtags=[
        'South',
    ],
    type=shared.SavedJobExecutorJobType.SCHEDULED_SEARCH,
)

res = s.saved_jobs.create(req)

if res.saved_jobs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [Union[shared.SavedJobCollection, shared.SavedJobExecutor, shared.SavedJobScheduledSearch]](../../models/shared/savedjob.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.CreateSavedJobsResponse](../../models/operations/createsavedjobsresponse.md)**


## get

Get a list of SavedJob objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_jobs.get()

if res.saved_jobs is not None:
    # handle response
    pass
```


### Response

**[operations.GetSavedJobsResponse](../../models/operations/getsavedjobsresponse.md)**

