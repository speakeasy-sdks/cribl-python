# Routes


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `comments`                                                                    | List[[components.Comments](../../models/components/comments.md)]              | :heavy_minus_sign:                                                            | Comments                                                                      |
| `groups`                                                                      | Dict[str, [components.RoutesGroups](../../models/components/routesgroups.md)] | :heavy_minus_sign:                                                            | N/A                                                                           |
| `id`                                                                          | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Routes ID                                                                     |
| `routes`                                                                      | List[[components.RoutesRoute](../../models/components/routesroute.md)]        | :heavy_check_mark:                                                            | Pipeline routing rules                                                        |