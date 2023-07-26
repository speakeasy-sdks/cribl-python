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
    id='7e13584f-7ae1-42c6-891f-82ce11571723',
    limit=52497,
    offset=347460,
    run_type='amet',
    state='voluptate',
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

