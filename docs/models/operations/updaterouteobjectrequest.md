# UpdateRouteObjectRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | There is only one route entity and it should be accessed with id: default. |
| `routes_input`                                                             | [Optional[shared.RoutesInput]](../../models/shared/routesinput.md)         | :heavy_minus_sign:                                                         | Routes object                                                              |