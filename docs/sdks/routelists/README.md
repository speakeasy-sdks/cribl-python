# RouteLists
(*.route_lists*)

### Available Operations

* [get](#get) - List all routes

## get

List all routes

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.route_lists.get()

if res.routes is not None:
    # handle response
    pass
```


### Response

**[operations.GetRouteListsResponse](../../models/operations/getroutelistsresponse.md)**

