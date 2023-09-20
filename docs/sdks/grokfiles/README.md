# GrokFiles

### Available Operations

* [get](#get) - Get a list of GrokFile objects

## get

Get a list of GrokFile objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.grok_files.get()

if res.grok_files is not None:
    # handle response
```


### Response

**[operations.GetGrokFilesResponse](../../models/operations/getgrokfilesresponse.md)**

