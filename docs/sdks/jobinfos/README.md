# JobInfos
(*job_infos*)

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
    collector_id='error',
    id='eee9526f-8d98-46e8-81ea-d4f0e1012563',
    limit=952143,
    offset=562783,
    run_type='magnam',
    state='saepe',
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

