# SavedJob
(*.saved_job*)

### Available Operations

* [delete](#delete) - Delete SavedJob
* [get](#get) - Get SavedJob by ID
* [update](#update) - Update SavedJob

## delete

Delete SavedJob

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_job.delete(id='string')

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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_job.get(id='string')

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
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_job.update(id='string', saved_job=components.SavedJobScheduledSearch(
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
    type=components.SavedJobScheduledSearchJobType.COLLECTION,
))

if res.saved_jobs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                               | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | Unique ID                                                                                                                                          |
| `saved_job`                                                                                                                                        | [Optional[Union[components.SavedJobCollection, components.SavedJobExecutor, components.SavedJobScheduledSearch]]](../../models/shared/savedjob.md) | :heavy_minus_sign:                                                                                                                                 | SavedJob object to be updated                                                                                                                      |


### Response

**[operations.UpdateSavedJobResponse](../../models/operations/updatesavedjobresponse.md)**

