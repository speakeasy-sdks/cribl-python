# RouteLists

### Available Operations

* [get](#get) - List all routes

## get

List all routes

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.route_lists.get()

if res.routes is not None:
    # handle response
```


### Response

**[operations.GetRouteListsResponse](../../models/operations/getroutelistsresponse.md)**

