# Job
(*job*)

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


res = s.job.cancel(id='Clifton')

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


res = s.job.delete(id='program')

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


res = s.job.get(id='female')

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


res = s.job.pause_job(id='white')

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


res = s.job.prevent(id='female')

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


res = s.job.resume(id='Balanced')

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

req = shared.SavedJobScheduledSearch(
    remove_fields=[
        'resist',
    ],
    saved_query_id='Cuyahoga pink disintermediate',
    schedule=shared.SavedJobScheduledSearchSchedule(
        run=shared.SavedJobScheduledSearchScheduleRunSettings(),
    ),
    streamtags=[
        'Soul',
    ],
    type=shared.SavedJobScheduledSearchJobType.EXECUTOR,
)

res = s.job.run_job(req)

if res.job_run is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [Union[shared.SavedJobCollection, shared.SavedJobExecutor, shared.SavedJobScheduledSearch]](../../models/shared/savedjob.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**

