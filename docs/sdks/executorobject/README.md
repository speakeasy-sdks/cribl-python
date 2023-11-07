# ExecutorObject
(*.executor_object*)

### Available Operations

* [get](#get) - Get a list of Executor objects

## get

Get a list of Executor objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.executor_object.get()

if res.executors is not None:
    # handle response
    pass
```


### Response

**[operations.GetExecutorObjectResponse](../../models/operations/getexecutorobjectresponse.md)**

