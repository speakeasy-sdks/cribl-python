# Changelogs

### Available Operations

* [get](#get) - Get changelog viewed state

## get

Get changelog viewed state

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.changelogs.get()

if res.changelog_states is not None:
    # handle response
```


### Response

**[operations.GetChangelogsResponse](../../models/operations/getchangelogsresponse.md)**

