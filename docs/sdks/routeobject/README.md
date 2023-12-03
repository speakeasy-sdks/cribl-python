# RouteObject
(*route_object*)

### Available Operations

* [update](#update) - Add, delete or update the routes with the required content.

## update

Add, delete or update the routes with the required content.

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.route_object.update(id='string', routes=components.RoutesInput(
    comments=[
        components.Comments(
            additional_properties={
                'key': 'string',
            },
        ),
    ],
    groups={
        'key': components.RoutesGroups(
            name='string',
        ),
    },
    routes=[
        components.RoutesRouteInput(
            additional_properties={
                'key': 'string',
            },
            name='string',
            pipeline='string',
        ),
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
| `routes`                                                                   | [Optional[components.RoutesInput]](../../models/components/routesinput.md) | :heavy_minus_sign:                                                         | Routes object                                                              |


### Response

**[operations.UpdateRouteObjectResponse](../../models/operations/updaterouteobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
