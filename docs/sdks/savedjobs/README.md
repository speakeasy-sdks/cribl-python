# SavedJobs

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
    environment='magni',
    executor=shared.SavedJobExecutorExecutor(
        conf=shared.SavedJobExecutorExecutorExecutorSpecificSettings(),
        store_task_results=False,
        type='deserunt',
    ),
    id='f923c594-9f83-4f35-8cf8-76ffb901c6ec',
    remove_fields=[
        'tempore',
    ],
    resume_on_boot=False,
    schedule=shared.SavedJobExecutorSchedule(
        cron_schedule='quidem',
        enabled=False,
        max_concurrent_runs=265930,
        resume_missed='voluptates',
        run=shared.SavedJobExecutorScheduleRunSettings(
            earliest=145435,
            expression='eius',
            job_timeout='sequi',
            latest=758194,
            log_level=shared.SavedJobExecutorScheduleRunSettingsLogLevel.SILLY,
            max_task_reschedule=459875,
            max_task_size='blanditiis',
            min_task_size='sint',
            mode='repellat',
            reschedule_dropped_tasks=False,
            time_range_type='a',
            timestamp_timezone='animi',
        ),
        skippable=False,
    ),
    streamtags=[
        'maiores',
    ],
    ttl='itaque',
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

