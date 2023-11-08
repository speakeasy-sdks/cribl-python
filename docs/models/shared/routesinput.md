# RoutesInput


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `comments`                                                                   | List[[components.Comments](../../models/shared/comments.md)]                 | :heavy_minus_sign:                                                           | Comments                                                                     |
| `groups`                                                                     | Dict[str, [components.RoutesGroups](../../models/shared/routesgroups.md)]    | :heavy_minus_sign:                                                           | N/A                                                                          |
| `id`                                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Routes ID                                                                    |
| `routes`                                                                     | List[[components.RoutesRouteInput](../../models/shared/routesrouteinput.md)] | :heavy_check_mark:                                                           | Pipeline routing rules                                                       |