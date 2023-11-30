# Processes
(*processes*)

### Available Operations

* [get](#get) - Get a list of processes under management

## get

Get a list of processes under management

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.processes.get()

if res.process_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetProcessesResponse](../../models/operations/getprocessesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
