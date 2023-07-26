# job_result

### Available Operations

* [get](#get) - Get results for a discover job by instance id

## get

Get results for a discover job by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.job_result.get('explicabo', 'ipsam', 583193)

if res.job_result is not None:
    # handle response
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `group`                                   | *str*                                     | :heavy_check_mark:                        | Group the job belongs to                  |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Instance id of the job to get results for |
| `max_files`                               | *Optional[int]*                           | :heavy_minus_sign:                        | Maximum files to get job results          |


### Response

**[operations.GetJobResultResponse](../../models/operations/getjobresultresponse.md)**

