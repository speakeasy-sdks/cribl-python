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
    bearer_auth="",
)


res = s.route_object.update(id='Van', routes=shared.Routes(
    comments=[
        {
            "East": 'male',
        },
    ],
    groups={
        "Metal": shared.RoutesGroups(
            name='Arizona Cotton extend',
        ),
    },
    routes=[
        {
            "Plastic": 'Carolina',
        },
    ],
))

if res.routes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | There is only one route entity and it should be accessed with id: default. |
| `routes`                                                                   | [Optional[shared.Routes]](../../models/shared/routes.md)                   | :heavy_minus_sign:                                                         | Routes object                                                              |


### Response

**[operations.UpdateRouteObjectResponse](../../models/operations/updaterouteobjectresponse.md)**

