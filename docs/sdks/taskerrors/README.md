# TaskErrors
(*task_errors*)

### Available Operations

* [get](#get) - Get Task errors for a job by id

## get

Get Task errors for a job by id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.task_errors.get(group='female', id='program')

if res.task_errors is not None:
    # handle response
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `group`                                   | *str*                                     | :heavy_check_mark:                        | Group the job belongs to                  |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Instance id of the job to get results for |


### Response

**[operations.GetTaskErrorsResponse](../../models/operations/gettaskerrorsresponse.md)**

