# Processes

### Available Operations

* [get](#get) - Get a list of processes under management

## get

Get a list of processes under management

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.processes.get()

if res.process_entries is not None:
    # handle response
```


### Response

**[operations.GetProcessesResponse](../../models/operations/getprocessesresponse.md)**

