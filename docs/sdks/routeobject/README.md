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


res = s.route_object.update(id='aspernatur', routes=shared.Routes(
    comments=[
        {
            "dicta": 'inventore',
            "ullam": 'iusto',
            "inventore": 'voluptate',
            "sed": 'dolorem',
        },
        {
            "exercitationem": 'amet',
        },
        {
            "voluptate": 'pariatur',
            "minus": 'a',
        },
        {
            "totam": 'cupiditate',
            "at": 'doloribus',
            "omnis": 'quam',
        },
    ],
    groups={
        "voluptates": shared.RoutesGroups(
            description='sequi',
            disabled=False,
            name='Gertrude Kautzer',
        ),
        "aperiam": shared.RoutesGroups(
            description='perspiciatis',
            disabled=False,
            name='Kellie Miller',
        ),
    },
    id='ddc5f111-dea1-4026-9541-a4d190feb217',
    routes=[
        {
            "distinctio": 'placeat',
        },
        {
            "eligendi": 'sit',
            "possimus": 'distinctio',
            "distinctio": 'assumenda',
            "illum": 'soluta',
        },
        {
            "laudantium": 'tempora',
            "esse": 'doloremque',
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

