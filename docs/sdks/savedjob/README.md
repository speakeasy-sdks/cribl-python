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

req = operations.DeleteSavedJobRequest(
    id='74ee5cfc-18ed-4c7f-b87e-32e04b3d3ed0',
)

res = s.saved_job.delete(req)

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteSavedJobRequest](../../models/operations/deletesavedjobrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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

req = operations.GetSavedJobRequest(
    id='c5670ef4-2bd3-4c9f-9cc5-03f6c39bcd0a',
)

res = s.saved_job.get(req)

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSavedJobRequest](../../models/operations/getsavedjobrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


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

req = operations.UpdateSavedJobRequest(
    request_body=shared.SavedJobExecutor(
        environment='qui',
        executor=shared.SavedJobExecutorExecutor(
            conf=shared.SavedJobExecutorExecutorExecutorSpecificSettings(),
            store_task_results=False,
            type='perspiciatis',
        ),
        id='0f957f38-5189-4ad7-af80-7aae03f33ca7',
        remove_fields=[
            'asperiores',
            'nam',
            'provident',
        ],
        resume_on_boot=False,
        schedule=shared.SavedJobExecutorSchedule(
            cron_schedule='fugiat',
            enabled=False,
            max_concurrent_runs=923442,
            resume_missed='non',
            run=shared.SavedJobExecutorScheduleRunSettings(
                earliest=12210,
                expression='neque',
                job_timeout='quia',
                latest=746232,
                log_level=shared.SavedJobExecutorScheduleRunSettingsLogLevel.DEBUG,
                max_task_reschedule=186488,
                max_task_size='commodi',
                min_task_size='a',
                mode='temporibus',
                reschedule_dropped_tasks=False,
                time_range_type='sequi',
                timestamp_timezone='eum',
            ),
            skippable=False,
        ),
        streamtags=[
            'expedita',
            'animi',
            'excepturi',
        ],
        ttl='dolores',
        type=shared.SavedJobExecutorJobType.COLLECTION,
    ),
    id='6bcb4158-35c7-4364-9723-133edc046bc5',
)

res = s.saved_job.update(req)

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateSavedJobRequest](../../models/operations/updatesavedjobrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateSavedJobResponse](../../models/operations/updatesavedjobresponse.md)**

