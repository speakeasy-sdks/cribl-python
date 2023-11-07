# JobStatus
(*.job_status*)

### Available Operations

* [get](#get) - Get job status

## get

Get job status

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job_status.get(id='string')

if res.search_job_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.GetJobStatusResponse](../../models/operations/getjobstatusresponse.md)**

