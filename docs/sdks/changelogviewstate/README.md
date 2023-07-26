# changelog_view_state

### Available Operations

* [update](#update) - Update changelog viewed state

## update

Update changelog viewed state

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.changelog_view_state.update()

if res.changelog_stateses is not None:
    # handle response
```


### Response

**[operations.UpdateChangelogViewStateResponse](../../models/operations/updatechangelogviewstateresponse.md)**

