# SavedJobs
(*.saved_jobs*)

### Available Operations

* [create](#create) - Create SavedJob
* [get](#get) - Get a list of SavedJob objects

## create

Create SavedJob

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.SavedJobExecutor(
    executor=components.SavedJobExecutorExecutor(
        conf=components.SavedJobExecutorExecutorSpecificSettings(),
        type='string',
    ),
    remove_fields=[
        'string',
    ],
    schedule=components.SavedJobExecutorSchedule(
        run=components.SavedJobExecutorRunSettings(),
    ),
    streamtags=[
        'string',
    ],
    type=components.SavedJobExecutorJobType.EXECUTOR,
)

res = s.saved_jobs.create(req)

if res.saved_jobs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [Union[components.SavedJobCollection, components.SavedJobExecutor, components.SavedJobScheduledSearch]](../../models/shared/savedjob.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.CreateSavedJobsResponse](../../models/operations/createsavedjobsresponse.md)**


## get

Get a list of SavedJob objects

### Example Usage

```python
import cribl

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

