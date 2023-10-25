# RoutesInput


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `comments`                                                        | List[[RoutesComments](../../models/shared/routescomments.md)]     | :heavy_minus_sign:                                                | Comments                                                          |
| `groups`                                                          | Dict[str, [RoutesGroups](../../models/shared/routesgroups.md)]    | :heavy_minus_sign:                                                | N/A                                                               |
| `id`                                                              | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Routes ID                                                         |
| `routes`                                                          | List[[RoutesRouteInput](../../models/shared/routesrouteinput.md)] | :heavy_check_mark:                                                | Pipeline routing rules                                            |