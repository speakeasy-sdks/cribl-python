# TaskError
(*task_error*)

### Available Operations

* [get](#get) - Get Task errors for a job by id

## get

Get Task errors for a job by id

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_error.get(id='<value>')

if res.task_errors is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Instance id of the job to get results for |


### Response

**[operations.GetTaskErrorResponse](../../models/operations/gettaskerrorresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
