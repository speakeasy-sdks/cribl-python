# ExportPackRequest


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `id`                                                      | *Optional[str]*                                           | :heavy_check_mark:                                        | Pack name                                                 |
| `mode`                                                    | *Optional[str]*                                           | :heavy_check_mark:                                        | Export mode, one of "merge_safe", "merge", "default_only" |
| `filename`                                                | *Optional[str]*                                           | :heavy_minus_sign:                                        | Filename of the exported Pack                             |