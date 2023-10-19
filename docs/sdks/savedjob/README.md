# SavedJob
(*saved_job*)

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
    bearer_auth="",
)


res = s.saved_job.delete(id='program')

if res.saved_jobs is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.saved_job.get(id='female')

if res.saved_jobs is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.saved_job.update(id='Van', saved_job=shared.SavedJobCollection(
    collector=shared.SavedJobCollectionCollector(
        conf=shared.SavedJobCollectionCollectorCollectorSpecificSettings(),
        type='Reactive',
    ),
    input=shared.SavedJobCollectionInput(
        breaker_rulesets=[
            'dock',
        ],
        metadata=[
            shared.SavedJobCollectionInputMetadata(
                name='Quality',
                value='redundant',
            ),
        ],
        preprocess=shared.SavedJobCollectionInputPreprocess(
            args=[
                'cheater',
            ],
        ),
    ),
    remove_fields=[
        'Islands',
    ],
    schedule=shared.SavedJobCollectionSchedule(
        run=shared.SavedJobCollectionScheduleRunSettings(),
    ),
    streamtags=[
        'online',
    ],
    type=shared.SavedJobCollectionJobType.EXECUTOR,
))

if res.saved_jobs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                   | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | Unique ID                                                                                                                              |
| `saved_job`                                                                                                                            | [Optional[Union[shared.SavedJobCollection, shared.SavedJobExecutor, shared.SavedJobScheduledSearch]]](../../models/shared/savedjob.md) | :heavy_minus_sign:                                                                                                                     | SavedJob object to be updated                                                                                                          |


### Response

**[operations.UpdateSavedJobResponse](../../models/operations/updatesavedjobresponse.md)**

