# ExecutorObject
(*executor_object*)

### Available Operations

* [get](#get) - Get a list of Executor objects

## get

Get a list of Executor objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.executor_object.get()

if res.executors is not None:
    # handle response
```


### Response

**[operations.GetExecutorObjectResponse](../../models/operations/getexecutorobjectresponse.md)**

