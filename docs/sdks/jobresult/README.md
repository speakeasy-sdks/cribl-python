# JobResult
(*job_result*)

### Available Operations

* [get](#get) - Get results for a discover job by instance id

## get

Get results for a discover job by instance id

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.job_result.get(group='<value>', id='<value>', max_files=700347)

if res.job_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `group`                                   | *str*                                     | :heavy_check_mark:                        | Group the job belongs to                  |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Instance id of the job to get results for |
| `max_files`                               | *Optional[int]*                           | :heavy_minus_sign:                        | Maximum files to get job results          |


### Response

**[operations.GetJobResultResponse](../../models/operations/getjobresultresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
