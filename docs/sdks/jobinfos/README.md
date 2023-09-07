# job_infos

### Available Operations

* [get](#get) - Get info on jobs

## get

Get info on jobs

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetJobInfosRequest(
    collector_id='quidem',
    id='e3e06080-7e2b-46e3-ab88-45f0597a60ff',
    limit=174658,
    offset=663866,
    run_type='minima',
    state='dolore',
)

res = s.job_infos.get(req)

if res.job_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetJobInfosRequest](../../models/operations/getjobinfosrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetJobInfosResponse](../../models/operations/getjobinfosresponse.md)**

