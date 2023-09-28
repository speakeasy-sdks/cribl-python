# RouteObject
(*route_object*)

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


res = s.route_object.update(id='laborum', routes=shared.Routes(
    comments=[
        {
            "dignissimos": 'vero',
        },
    ],
    groups={
        "qui": shared.RoutesGroups(
            description='consectetur',
            disabled=False,
            name='Roy Christiansen',
        ),
    },
    id='411faf4b-7544-4e47-ae80-2857a5b40463',
    routes=[
        {
            "mollitia": 'dignissimos',
        },
    ],
))

if res.routes is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | There is only one route entity and it should be accessed with id: default. |
| `routes`                                                                   | [Optional[shared.Routes]](../../models/shared/routes.md)                   | :heavy_minus_sign:                                                         | Routes object                                                              |


### Response

**[operations.UpdateRouteObjectResponse](../../models/operations/updaterouteobjectresponse.md)**

