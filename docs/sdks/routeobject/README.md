# RouteObject

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


res = s.route_object.update(id='nemo', routes=shared.Routes(
    comments=[
        {
            "culpa": 'consequuntur',
        },
    ],
    groups={
        "amet": shared.RoutesGroups(
            description='deserunt',
            disabled=False,
            name='Sally Schmidt',
        ),
    },
    id='c5fde10a-0ce2-4169-a510-019c6dc5e347',
    routes=[
        {
            "laboriosam": 'sed',
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

