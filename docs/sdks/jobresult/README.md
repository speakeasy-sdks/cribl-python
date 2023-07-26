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

req = operations.GetJobResultRequest(
    group='voluptate',
    id='dcfa89df-975e-4356-a860-92e9c3ddc5f1',
    max_files=114212,
)

res = s.job_result.get(req)

if res.job_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetJobResultRequest](../../models/operations/getjobresultrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetJobResultResponse](../../models/operations/getjobresultresponse.md)**

