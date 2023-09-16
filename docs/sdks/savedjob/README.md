# SavedJob

### Available Operations

* [delete](#delete) - Delete SavedJob
* [get](#get) - Get SavedJob by ID
* [update](#update) - Update SavedJob

## delete

Delete SavedJob

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_job.delete(id='eaque')

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteSavedJobResponse](../../models/operations/deletesavedjobresponse.md)**


## get

Get SavedJob by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_job.get(id='architecto')

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetSavedJobResponse](../../models/operations/getsavedjobresponse.md)**


## update

Update SavedJob

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_job.update(id='similique', request_body=shared.SavedJobScheduledSearch(
    environment='blanditiis',
    id='02e2ec09-ff8f-40f8-96ff-3477c13e902c',
    remove_fields=[
        'beatae',
    ],
    resume_on_boot=False,
    saved_query_id='incidunt',
    schedule=shared.SavedJobScheduledSearchSchedule(
        cron_schedule='dicta',
        enabled=False,
        max_concurrent_runs=139133,
        resume_missed='corporis',
        run=shared.SavedJobScheduledSearchScheduleRunSettings(
            earliest=701441,
            expression='alias',
            job_timeout='error',
            latest=424854,
            log_level=shared.SavedJobScheduledSearchScheduleRunSettingsLogLevel.ERROR,
            max_task_reschedule=664197,
            max_task_size='laboriosam',
            min_task_size='ex',
            mode='quas',
            reschedule_dropped_tasks=False,
            time_range_type='veritatis',
            timestamp_timezone='ullam',
        ),
        skippable=False,
    ),
    streamtags=[
        'quae',
    ],
    ttl='similique',
    type=shared.SavedJobScheduledSearchJobType.COLLECTION,
))

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `id`                          | *str*                         | :heavy_check_mark:            | Unique ID                     |
| `request_body`                | *Optional[Any]*               | :heavy_minus_sign:            | SavedJob object to be updated |


### Response

**[operations.UpdateSavedJobResponse](../../models/operations/updatesavedjobresponse.md)**

