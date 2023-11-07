# Job
(*.job*)

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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job.cancel(id='string')

if res.job_cancel is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job.delete(id='string')

if res.job_delete is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job.get(id='string')

if res.job_infos is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job.pause_job(id='string')

if res.job_pause is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job.prevent(id='string')

if res.job_infos is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job.resume(id='string')

if res.job_resume is not None:
    # handle response
    pass
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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.SavedJobScheduledSearch(
    remove_fields=[
        'string',
    ],
    saved_query_id='string',
    schedule=components.SavedJobScheduledSearchSchedule(
        run=components.SavedJobScheduledSearchRunSettings(),
    ),
    streamtags=[
        'string',
    ],
    type=components.SavedJobScheduledSearchJobType.SCHEDULED_SEARCH,
)

res = s.job.run_job(req)

if res.job_run is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [Union[components.SavedJobCollection, components.SavedJobExecutor, components.SavedJobScheduledSearch]](../../models/shared/savedjob.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**

