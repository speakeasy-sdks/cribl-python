# TaskErrors
(*task_errors*)

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


res = s.task_errors.get(group='<value>', id='<value>')

if res.task_errors is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `group`                                   | *str*                                     | :heavy_check_mark:                        | Group the job belongs to                  |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Instance id of the job to get results for |


### Response

**[operations.GetTaskErrorsResponse](../../models/operations/gettaskerrorsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
