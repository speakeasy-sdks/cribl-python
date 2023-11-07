# TaskErrors
(*.task_errors*)

### Available Operations

* [get](#get) - Get Task errors for a job by id

## get

Get Task errors for a job by id

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.task_errors.get(group='string', id='string')

if res.task_errors is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `group`                                   | *str*                                     | :heavy_check_mark:                        | Group the job belongs to                  |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Instance id of the job to get results for |


### Response

**[operations.GetTaskErrorsResponse](../../models/operations/gettaskerrorsresponse.md)**

