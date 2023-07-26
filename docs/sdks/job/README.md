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

req = operations.CancelJobRequest(
    id='d364ffd4-5590-46d1-a63d-48e935c2c9e8',
)

res = s.job.cancel(req)

if res.job_cancel is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CancelJobRequest](../../models/operations/canceljobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


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

req = operations.DeleteJobRequest(
    id='1f30be3e-4320-42d7-a165-76506641870d',
)

res = s.job.delete(req)

if res.job_delete is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.DeleteJobRequest](../../models/operations/deletejobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


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

req = operations.GetJobRequest(
    id='9d21f9ad-030c-44ec-811a-0836429068b8',
)

res = s.job.get(req)

if res.job_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetJobRequest](../../models/operations/getjobrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


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

req = operations.PauseJobRequest(
    id='502a55e7-f73b-4c84-9e32-0a319f4badf9',
)

res = s.job.pause_job(req)

if res.job_pause is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.PauseJobRequest](../../models/operations/pausejobrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


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

req = operations.PreventJobRequest(
    id='47c9a867-bc42-4426-a658-16ddca8ef51f',
)

res = s.job.prevent(req)

if res.job_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.PreventJobRequest](../../models/operations/preventjobrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


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

req = operations.ResumeJobRequest(
    id='cb4c593e-c12c-4daa-90ec-7afedbd80df4',
)

res = s.job.resume(req)

if res.job_resume is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ResumeJobRequest](../../models/operations/resumejobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


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

req = shared.SavedJobCollection(
    collector=shared.SavedJobCollectionCollector(
        conf=shared.SavedJobCollectionCollectorCollectorSpecificSettings(),
        destructive=False,
        type='corrupti',
    ),
    environment='similique',
    id='47f9390c-5888-4098-bdab-f9ef3ffdd9f7',
    input=shared.SavedJobCollectionInput(
        breaker_rulesets=[
            'aut',
            'quam',
            'omnis',
            'similique',
        ],
        metadata=[
            shared.SavedJobCollectionInputMetadata(
                name='Muriel Durgan',
                value='sed',
            ),
            shared.SavedJobCollectionInputMetadata(
                name='Francis Stehr DVM',
                value='labore',
            ),
            shared.SavedJobCollectionInputMetadata(
                name='Mr. Jesse Luettgen',
                value='iusto',
            ),
            shared.SavedJobCollectionInputMetadata(
                name='Jon Kertzmann',
                value='magnam',
            ),
        ],
        output='accusamus',
        pipeline='nulla',
        preprocess=shared.SavedJobCollectionInputPreprocess(
            args=[
                'quibusdam',
                'praesentium',
                'enim',
                'animi',
            ],
            command='unde',
            disabled=False,
        ),
        send_to_routes=False,
        stale_channel_flush_ms=61498,
        throttle_rate_per_sec='eum',
        type=shared.SavedJobCollectionInputType.COLLECTION,
    ),
    remove_fields=[
        'eveniet',
        'laboriosam',
    ],
    resume_on_boot=False,
    schedule=shared.SavedJobCollectionSchedule(
        cron_schedule='ratione',
        enabled=False,
        max_concurrent_runs=505473,
        resume_missed='quidem',
        run=shared.SavedJobCollectionScheduleRunSettings(
            earliest=848649,
            expression='reiciendis',
            job_timeout='placeat',
            latest=175275,
            log_level=shared.SavedJobCollectionScheduleRunSettingsLogLevel.ERROR,
            max_task_reschedule=201966,
            max_task_size='quia',
            min_task_size='quidem',
            mode='voluptas',
            reschedule_dropped_tasks=False,
            time_range_type='quo',
            timestamp_timezone='laudantium',
        ),
        skippable=False,
    ),
    streamtags=[
        'omnis',
        'omnis',
    ],
    ttl='fugit',
    type=shared.SavedJobCollectionJobType.COLLECTION,
    worker_affinity=False,
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

