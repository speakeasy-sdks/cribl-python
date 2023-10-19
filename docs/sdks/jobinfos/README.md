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
    bearer_auth="",
)

req = operations.GetJobInfosRequest()

res = s.job_infos.get(req)

if res.job_infos is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetJobInfosRequest](../../models/operations/getjobinfosrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetJobInfosResponse](../../models/operations/getjobinfosresponse.md)**

