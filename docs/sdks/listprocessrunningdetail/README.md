# ListProcessRunningDetail
(*list_process_running_detail*)

### Available Operations

* [get](#get) - Get a detailed list of processes running on the edge host

## get

Get a detailed list of processes running on the edge host

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_process_running_detail.get()

if res.processes is not None:
    # handle response
    pass
```


### Response

**[operations.GetListProcessRunningDetailResponse](../../models/operations/getlistprocessrunningdetailresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
