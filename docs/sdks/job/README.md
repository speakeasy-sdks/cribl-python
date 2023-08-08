# job

### Available Operations

* [cancel](#cancel) - Cancel a job by instance id
* [delete](#delete) - Remove job from job inspector by instance id
* [get](#get) - Get job info by instance id
* [pause_job](#pause_job) - Pause a job by instance id
* [prevent](#prevent) - prevent job from being deleted automatically
* [resume](#resume) - Resume a job by instance id
* [run_job](#run_job) - Run or schedule a job

## cancel

Cancel a job by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job.cancel(id='voluptatibus')

if res.job_cancel is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job instance id    |


### Response

**[operations.CancelJobResponse](../../models/operations/canceljobresponse.md)**


## delete

Remove job from job inspector by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job.delete(id='molestias')

if res.job_delete is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job instance id    |


### Response

**[operations.DeleteJobResponse](../../models/operations/deletejobresponse.md)**


## get

Get job info by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job.get(id='officia')

if res.job_infos is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job instance id    |


### Response

**[operations.GetJobResponse](../../models/operations/getjobresponse.md)**


## pause_job

Pause a job by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job.pause_job(id='libero')

if res.job_pause is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job instance id    |


### Response

**[operations.PauseJobResponse](../../models/operations/pausejobresponse.md)**


## prevent

prevent job from being deleted automatically

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job.prevent(id='totam')

if res.job_infos is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job Instance id    |


### Response

**[operations.PreventJobResponse](../../models/operations/preventjobresponse.md)**


## resume

Resume a job by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job.resume(id='sequi')

if res.job_resume is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job instance id    |


### Response

**[operations.ResumeJobResponse](../../models/operations/resumejobresponse.md)**


## run_job

Run or schedule a job

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
    environment='ea',
    executor=shared.SavedJobExecutorExecutor(
        conf=shared.SavedJobExecutorExecutorExecutorSpecificSettings(),
        store_task_results=False,
        type='impedit',
    ),
    id='723ffda9-e06b-4ee4-825c-1fc0e115c80b',
    remove_fields=[
        'a',
        'iste',
        'dicta',
        'quos',
    ],
    resume_on_boot=False,
    schedule=shared.SavedJobExecutorSchedule(
        cron_schedule='ullam',
        enabled=False,
        max_concurrent_runs=295950,
        resume_missed='modi',
        run=shared.SavedJobExecutorScheduleRunSettings(
            earliest=929292,
            expression='maxime',
            job_timeout='modi',
            latest=163558,
            log_level=shared.SavedJobExecutorScheduleRunSettingsLogLevel.SILLY,
            max_task_reschedule=876840,
            max_task_size='doloribus',
            min_task_size='impedit',
            mode='porro',
            reschedule_dropped_tasks=False,
            time_range_type='accusamus',
            timestamp_timezone='totam',
        ),
        skippable=False,
    ),
    streamtags=[
        'ab',
        'sint',
        'nihil',
        'esse',
    ],
    ttl='iure',
    type=shared.SavedJobExecutorJobType.EXECUTOR,
)

res = s.job.run_job(req)

if res.job_run is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**

