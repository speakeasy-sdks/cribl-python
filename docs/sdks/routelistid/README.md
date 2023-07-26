# route_list_id

### Available Operations

* [get](#get) - List all routes by id

## get

List all routes by id

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetRouteListIDRequest(
    id='548568a0-424e-400a-9d6e-b9434645d030',
)

res = s.route_list_id.get(req)

if res.routes is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetRouteListIDRequest](../../models/operations/getroutelistidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetRouteListIDResponse](../../models/operations/getroutelistidresponse.md)**

