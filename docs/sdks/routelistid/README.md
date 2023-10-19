# RouteListID
(*route_list_id*)

### Available Operations

* [get](#get) - List all routes by id

## get

List all routes by id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.route_list_id.get(id='female')

if res.routes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | There is only one route entity and it should be accessed with id: default. |


### Response

**[operations.GetRouteListIDResponse](../../models/operations/getroutelistidresponse.md)**

