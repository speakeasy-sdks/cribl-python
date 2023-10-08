# RemoteRepo
(*remote_repo*)

### Available Operations

* [sync](#sync) - syncs with remote repo via POST requests

## sync

syncs with remote repo via POST requests

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.remote_repo.sync()

if res.git_status_results is not None:
    # handle response
```


### Response

**[operations.SyncRemoteRepoResponse](../../models/operations/syncremotereporesponse.md)**

