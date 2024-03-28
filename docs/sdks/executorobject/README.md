# ExecutorObject
(*executor_object*)

### Available Operations

* [get](#get) - Get a list of Executor objects

## get

Get a list of Executor objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.executor_object.get()

if res.executors is not None:
    # handle response
    pass

```


### Response

**[operations.GetExecutorObjectResponse](../../models/operations/getexecutorobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
