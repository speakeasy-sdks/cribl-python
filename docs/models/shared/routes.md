# Routes


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `comments`                                                     | list[dict[str, *Any*]]                                         | :heavy_minus_sign:                                             | Comments                                                       |
| `groups`                                                       | dict[str, [RoutesGroups](../../models/shared/routesgroups.md)] | :heavy_minus_sign:                                             | N/A                                                            |
| `id`                                                           | *Optional[str]*                                                | :heavy_minus_sign:                                             | Routes ID                                                      |
| `routes`                                                       | list[dict[str, *Any*]]                                         | :heavy_check_mark:                                             | Pipeline routing rules                                         |