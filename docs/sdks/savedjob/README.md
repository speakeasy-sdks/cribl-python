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


res = s.saved_job.delete(id='cum')

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


res = s.saved_job.get(id='aspernatur')

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


res = s.saved_job.update(id='libero', request_body=shared.SavedJobScheduledSearch(
    environment='incidunt',
    id='ecae6c3d-5db3-4ade-bd5d-aea4c506a8aa',
    remove_fields=[
        'occaecati',
    ],
    resume_on_boot=False,
    saved_query_id='labore',
    schedule=shared.SavedJobScheduledSearchSchedule(
        cron_schedule='quo',
        enabled=False,
        max_concurrent_runs=19462,
        resume_missed='fugit',
        run=shared.SavedJobScheduledSearchScheduleRunSettings(
            earliest=399222,
            expression='magnam',
            job_timeout='quaerat',
            latest=755868,
            log_level=shared.SavedJobScheduledSearchScheduleRunSettingsLogLevel.SILLY,
            max_task_reschedule=342921,
            max_task_size='officiis',
            min_task_size='unde',
            mode='nulla',
            reschedule_dropped_tasks=False,
            time_range_type='error',
            timestamp_timezone='mollitia',
        ),
        skippable=False,
    ),
    streamtags=[
        'magnam',
    ],
    ttl='nostrum',
    type=shared.SavedJobScheduledSearchJobType.EXECUTOR,
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

