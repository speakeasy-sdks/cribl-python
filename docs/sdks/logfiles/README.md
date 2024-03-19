# LogFiles
(*log_files*)

### Available Operations

* [get](#get) - Get a list of log files

## get

Get a list of log files

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.log_files.get()

if res.log_files_info is not None:
    # handle response
    pass

```


### Response

**[operations.GetLogFilesResponse](../../models/operations/getlogfilesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
