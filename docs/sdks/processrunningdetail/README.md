# ProcessRunningDetail
(*process_running_detail*)

### Available Operations

* [get](#get) - Get details of a process running on the edge host

## get

Get details of a process running on the edge host

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.process_running_detail.get(pid='string')

if res.processes is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `pid`              | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetProcessRunningDetailResponse](../../models/operations/getprocessrunningdetailresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
