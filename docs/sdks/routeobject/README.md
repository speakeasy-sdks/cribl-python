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


res = s.route_object.update(id='nemo', routes=shared.Routes(
    comments=[
        {
            "illum": 'facilis',
        },
    ],
    groups={
        "non": shared.RoutesGroups(
            description='mollitia',
            disabled=False,
            name='Clay Reichel',
        ),
    },
    id='daea4c50-6a8a-4a94-8026-44cf5e9d9a45',
    routes=[
        {
            "esse": 'corrupti',
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

