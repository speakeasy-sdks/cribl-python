# job_results

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

req = operations.GetJobResultsRequest(
    id='1dea1026-d541-4a4d-990f-eb21780bccc0',
)

res = s.job_results.get(req)

if res.get_job_results_200_application_x_ndjson_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetJobResultsRequest](../../models/operations/getjobresultsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetJobResultsResponse](../../models/operations/getjobresultsresponse.md)**

