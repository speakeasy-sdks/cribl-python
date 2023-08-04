# saved_job

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


res = s.saved_job.delete(id='impedit')

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


res = s.saved_job.get(id='recusandae')

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


res = s.saved_job.update(id='voluptate', request_body=shared.SavedJobExecutor(
    environment='est',
    executor=shared.SavedJobExecutorExecutor(
        conf=shared.SavedJobExecutorExecutorExecutorSpecificSettings(),
        store_task_results=False,
        type='et',
    ),
    id='bd8fb7a0-a116-4ce7-a3d4-097fa30e9af7',
    remove_fields=[
        'ipsam',
    ],
    resume_on_boot=False,
    schedule=shared.SavedJobExecutorSchedule(
        cron_schedule='libero',
        enabled=False,
        max_concurrent_runs=153942,
        resume_missed='omnis',
        run=shared.SavedJobExecutorScheduleRunSettings(
            earliest=120646,
            expression='qui',
            job_timeout='explicabo',
            latest=6203,
            log_level=shared.SavedJobExecutorScheduleRunSettingsLogLevel.WARN,
            max_task_reschedule=9284,
            max_task_size='fugiat',
            min_task_size='voluptatum',
            mode='velit',
            reschedule_dropped_tasks=False,
            time_range_type='hic',
            timestamp_timezone='ullam',
        ),
        skippable=False,
    ),
    streamtags=[
        'itaque',
        'distinctio',
        'iusto',
    ],
    ttl='dignissimos',
    type=shared.SavedJobExecutorJobType.EXECUTOR,
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

