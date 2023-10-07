# CurrentConfig
(*current_config*)

### Available Operations

* [push](#push) - push the current configs to the remote repository.

## push

push the current configs to the remote repository.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.current_config.push()

if res.push_config is not None:
    # handle response
```


### Response

**[operations.PushCurrentConfigResponse](../../models/operations/pushcurrentconfigresponse.md)**

