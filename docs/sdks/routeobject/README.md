# route_object

### Available Operations

* [update](#update) - Add, delete or update the routes with the required content.

## update

Add, delete or update the routes with the required content.

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateRouteObjectRequest(
    routes=shared.Routes(
        comments=[
            {
                "repellat": 'expedita',
                "libero": 'mollitia',
            },
            {
                "cumque": 'cumque',
                "vero": 'a',
            },
            {
                "ipsam": 'quod',
                "facilis": 'doloremque',
                "illo": 'reiciendis',
                "debitis": 'enim',
            },
        ],
        groups={
            "accusamus": shared.RoutesGroups(
                description='ipsam',
                disabled=False,
                name='Kay O'Kon',
            ),
        },
        id='ac82b85f-8bc2-4cab-a8da-4127dd597ff4',
        routes=[
            {
                "inventore": 'similique',
            },
            {
                "et": 'distinctio',
                "porro": 'nihil',
                "numquam": 'rerum',
            },
        ],
    ),
    id='86cecc74-f77b-4484-8bd6-a6f0441d2c3b',
)

res = s.route_object.update(req)

if res.routes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateRouteObjectRequest](../../models/operations/updaterouteobjectrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateRouteObjectResponse](../../models/operations/updaterouteobjectresponse.md)**

