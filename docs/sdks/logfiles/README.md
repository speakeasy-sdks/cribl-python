# LogFiles

### Available Operations

* [get](#get) - Get a list of log files

## get

Get a list of log files

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.log_files.get()

if res.log_files_info is not None:
    # handle response
```


### Response

**[operations.GetLogFilesResponse](../../models/operations/getlogfilesresponse.md)**

