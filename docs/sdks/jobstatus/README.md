# job_status

### Available Operations

* [get](#get) - Get job status

## get

Get job status

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetJobStatusRequest(
    id='dbbddb48-4708-4fb4-a391-e6bc158c4c4e',
)

res = s.job_status.get(req)

if res.search_job_status is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetJobStatusRequest](../../models/operations/getjobstatusrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetJobStatusResponse](../../models/operations/getjobstatusresponse.md)**

