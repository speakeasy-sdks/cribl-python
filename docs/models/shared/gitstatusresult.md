# GitStatusResult


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `ahead`                                                    | *int*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `behind`                                                   | *int*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `conflicted`                                               | List[*str*]                                                | :heavy_check_mark:                                         | N/A                                                        |
| `created`                                                  | List[*str*]                                                | :heavy_check_mark:                                         | N/A                                                        |
| `current`                                                  | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `deleted`                                                  | List[*str*]                                                | :heavy_check_mark:                                         | N/A                                                        |
| `files`                                                    | List[[components.Files](../../models/shared/files.md)]     | :heavy_check_mark:                                         | N/A                                                        |
| `modified`                                                 | List[*str*]                                                | :heavy_check_mark:                                         | N/A                                                        |
| `not_added`                                                | List[*str*]                                                | :heavy_check_mark:                                         | N/A                                                        |
| `renamed`                                                  | List[[components.Renamed](../../models/shared/renamed.md)] | :heavy_check_mark:                                         | N/A                                                        |
| `staged`                                                   | List[*str*]                                                | :heavy_check_mark:                                         | N/A                                                        |
| `tracking`                                                 | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |