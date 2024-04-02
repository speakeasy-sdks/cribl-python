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

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saved_job.delete(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get

Get SavedJob by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saved_job.get(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## update

Update SavedJob

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saved_job.update(id='<value>', saved_job=components.SavedJobScheduledSearch(
    saved_query_id='<value>',
    type=components.SavedJobScheduledSearchJobType.COLLECTION,
))

if res.saved_jobs is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                   | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | Unique ID                                                                                                                                              |
| `saved_job`                                                                                                                                            | [Optional[Union[components.SavedJobCollection, components.SavedJobExecutor, components.SavedJobScheduledSearch]]](../../models/components/savedjob.md) | :heavy_minus_sign:                                                                                                                                     | SavedJob object to be updated                                                                                                                          |


### Response

**[operations.UpdateSavedJobResponse](../../models/operations/updatesavedjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
