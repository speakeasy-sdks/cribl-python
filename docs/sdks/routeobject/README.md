# RouteObject
(*route_object*)

### Available Operations

* [update](#update) - Add, delete or update the routes with the required content.

## update

Add, delete or update the routes with the required content.

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.route_object.update(id='<value>', routes=components.RoutesInput(
    routes=[
        components.RoutesRouteInput(
            name='<value>',
            pipeline='<value>',
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
| errors.SDKError  | 4x-5xx           | */*              |
