# JobResults
(*job_results*)

### Available Operations

* [get](#get) - Get results for a discover job by instance id

## get

Get results for a discover job by instance id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.job_results.get(id='female')

if res.get_job_results_200_application_x_ndjson_binary_string is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Job instance id    |


### Response

**[operations.GetJobResultsResponse](../../models/operations/getjobresultsresponse.md)**

