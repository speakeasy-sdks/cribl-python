# search_jobs

### Available Operations

* [get](#get) - Get a list of SearchJob objects

## get

Get a list of SearchJob objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.search_jobs.get()

if res.search_jobs is not None:
    # handle response
```


### Response

**[operations.GetSearchJobsResponse](../../models/operations/getsearchjobsresponse.md)**

