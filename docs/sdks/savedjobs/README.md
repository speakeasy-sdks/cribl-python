# saved_jobs

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SavedJobExecutor(
    environment='assumenda',
    executor=shared.SavedJobExecutorExecutor(
        conf=shared.SavedJobExecutorExecutorExecutorSpecificSettings(),
        store_task_results=False,
        type='sunt',
    ),
    id='2e8c1f84-9382-45fd-842c-876c2c2dfb4c',
    remove_fields=[
        'quo',
        'illo',
        'nobis',
        'esse',
    ],
    resume_on_boot=False,
    schedule=shared.SavedJobExecutorSchedule(
        cron_schedule='nisi',
        enabled=False,
        max_concurrent_runs=129619,
        resume_missed='sequi',
        run=shared.SavedJobExecutorScheduleRunSettings(
            earliest=4787,
            expression='reiciendis',
            job_timeout='quos',
            latest=256310,
            log_level=shared.SavedJobExecutorScheduleRunSettingsLogLevel.ERROR,
            max_task_reschedule=980376,
            max_task_size='nam',
            min_task_size='architecto',
            mode='rerum',
            reschedule_dropped_tasks=False,
            time_range_type='assumenda',
            timestamp_timezone='eos',
        ),
        skippable=False,
    ),
    streamtags=[
        'hic',
    ],
    ttl='repellendus',
    type=shared.SavedJobExecutorJobType.SCHEDULED_SEARCH,
)

res = s.saved_jobs.create(req)

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateSavedJobsResponse](../../models/operations/createsavedjobsresponse.md)**


## get

Get a list of SavedJob objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_jobs.get()

if res.saved_jobs is not None:
    # handle response
```


### Response

**[operations.GetSavedJobsResponse](../../models/operations/getsavedjobsresponse.md)**

